"""Minimal stdlib TikHub MCP-over-HTTP client.

This is vendored so the compliance skill can run optional Xiaohongshu live
evidence search without depending on another local repository.
"""

from __future__ import annotations

import json
import os
import sys
import time
import urllib.error
import urllib.request
from pathlib import Path
from typing import Any

ENDPOINT = "https://mcp.tikhub.io/{platform}/mcp"
HEALTH_URL = "https://mcp.tikhub.io/health"
PLATFORMS_URL = "https://mcp.tikhub.io/platforms"
SESSION_DIR = Path("/tmp")
SESSION_TTL_SECONDS = 300

ENV_VAR = "TIKHUB_API_KEY"
PROTOCOL_VERSION = "2024-11-05"
CLIENT_NAME = "self-media-compliance-tikhub"
CLIENT_VERSION = "0.1.0"
USER_AGENT = f"{CLIENT_NAME}/{CLIENT_VERSION} (+https://mcp.tikhub.io)"
DEBUG = os.environ.get("TIKHUB_DEBUG") == "1"


class TikhubError(Exception):
    """Raised on TikHub transport or protocol errors."""


def _debug(message: str) -> None:
    if DEBUG:
        print(f"[tikhub] {message}", file=sys.stderr)


def _env_files() -> list[Path]:
    custom = os.environ.get("TIKHUB_ENV_FILE")
    files = [Path(custom)] if custom else []
    if os.environ.get("TIKHUB_NO_ENV_FILE") != "1":
        files.append(Path.home() / ".claude" / ".env")
    return files


def load_api_key() -> str:
    key = os.environ.get(ENV_VAR)
    if key:
        return key.strip()
    for env_file in _env_files():
        if not env_file.is_file():
            continue
        for line in env_file.read_text().splitlines():
            line = line.strip()
            if not line or line.startswith("#") or "=" not in line:
                continue
            name, value = line.split("=", 1)
            if name.strip() == ENV_VAR:
                value = value.strip().strip('"').strip("'")
                if value:
                    return value
    searched = ", ".join(str(path) for path in _env_files()) or "no env files"
    raise TikhubError(f"missing {ENV_VAR}. Set env var or add `{ENV_VAR}=...` to one of: {searched}")


def _parse_sse(body: bytes) -> dict:
    text = body.decode("utf-8", errors="replace")
    for line in text.splitlines():
        if line.startswith("data:"):
            payload = line[len("data:") :].strip()
            if payload:
                try:
                    return json.loads(payload)
                except json.JSONDecodeError as exc:
                    raise TikhubError(f"bad SSE JSON: {exc}") from exc
    try:
        return json.loads(text)
    except json.JSONDecodeError as exc:
        raise TikhubError(f"no SSE data in response. raw: {text[:500]}") from exc


def _maybe_unwrap_text(value: Any) -> Any:
    if isinstance(value, str):
        text = value.strip()
        if text and text[0] in "{[":
            try:
                return json.loads(text)
            except json.JSONDecodeError:
                return value
    return value


class TikhubClient:
    def __init__(self, platform: str, api_key: str | None = None, timeout: int = 60):
        self.platform = platform
        self.endpoint = ENDPOINT.format(platform=platform)
        self.api_key = api_key or load_api_key()
        self.timeout = timeout
        self._req_id = 0

    @property
    def _session_file(self) -> Path:
        return SESSION_DIR / f".tikhub-session-{self.platform}.json"

    def _next_id(self) -> int:
        self._req_id += 1
        return self._req_id

    def _load_session(self) -> str | None:
        if not self._session_file.is_file():
            return None
        try:
            data = json.loads(self._session_file.read_text())
        except (OSError, json.JSONDecodeError):
            return None
        if time.time() - data.get("created_at", 0) > SESSION_TTL_SECONDS:
            return None
        return data.get("session_id")

    def _save_session(self, session_id: str) -> None:
        try:
            self._session_file.write_text(json.dumps({"session_id": session_id, "created_at": time.time()}))
        except OSError as exc:
            _debug(f"could not cache session: {exc}")

    def _drop_session(self) -> None:
        try:
            self._session_file.unlink(missing_ok=True)
        except OSError:
            pass

    def _post(self, payload: dict, session_id: str | None) -> tuple[dict, dict]:
        body = json.dumps(payload).encode("utf-8")
        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json",
            "Accept": "application/json, text/event-stream",
            "User-Agent": USER_AGENT,
        }
        if session_id:
            headers["Mcp-Session-Id"] = session_id
        req = urllib.request.Request(self.endpoint, data=body, headers=headers, method="POST")
        try:
            with urllib.request.urlopen(req, timeout=self.timeout) as resp:
                resp_body = resp.read()
                resp_headers = {k.lower(): v for k, v in resp.headers.items()}
        except urllib.error.HTTPError as exc:
            err_body = exc.read().decode("utf-8", errors="replace") if exc.fp else ""
            raise TikhubError(f"HTTP {exc.code}: {err_body[:500]}") from exc
        except TimeoutError as exc:
            raise TikhubError(f"network timeout: {exc}") from exc
        except urllib.error.URLError as exc:
            raise TikhubError(f"network error: {exc.reason}") from exc
        return _parse_sse(resp_body), resp_headers

    def initialize(self) -> str:
        payload = {
            "jsonrpc": "2.0",
            "id": self._next_id(),
            "method": "initialize",
            "params": {
                "protocolVersion": PROTOCOL_VERSION,
                "capabilities": {},
                "clientInfo": {"name": CLIENT_NAME, "version": CLIENT_VERSION},
            },
        }
        data, headers = self._post(payload, session_id=None)
        if "error" in data:
            raise TikhubError(f"initialize failed: {data['error']}")
        session_id = headers.get("mcp-session-id")
        if not session_id:
            raise TikhubError("initialize: server did not return mcp-session-id header")
        self._save_session(session_id)
        return session_id

    def _ensure_session(self) -> str:
        return self._load_session() or self.initialize()

    def _call_jsonrpc(self, method: str, params: dict) -> Any:
        for attempt in (1, 2):
            session_id = self._ensure_session()
            payload = {"jsonrpc": "2.0", "id": self._next_id(), "method": method, "params": params}
            try:
                data, _headers = self._post(payload, session_id=session_id)
            except TikhubError as exc:
                message = str(exc).lower()
                if attempt == 1 and ("session" in message or "401" in message or "440" in message):
                    self._drop_session()
                    continue
                raise
            if "error" in data:
                error = data["error"]
                if attempt == 1 and isinstance(error, dict) and "session" in (error.get("message") or "").lower():
                    self._drop_session()
                    continue
                raise TikhubError(f"{method} failed: {error}")
            return data.get("result")
        raise TikhubError(f"{method} failed after retry")

    def call(self, tool_name: str, arguments: dict | None = None) -> Any:
        result = self._call_jsonrpc("tools/call", {"name": tool_name, "arguments": arguments or {}})
        if not isinstance(result, dict):
            return result
        if "structuredContent" in result and result["structuredContent"] is not None:
            structured = result["structuredContent"]
            if isinstance(structured, dict) and set(structured) == {"result"}:
                return _maybe_unwrap_text(structured["result"])
            return structured
        content = result.get("content")
        if isinstance(content, list) and content:
            first = content[0]
            if isinstance(first, dict) and first.get("type") == "text":
                return _maybe_unwrap_text(first.get("text", ""))
        return result


def _get_json(url: str, label: str) -> Any:
    req = urllib.request.Request(url, headers={"User-Agent": USER_AGENT})
    try:
        with urllib.request.urlopen(req, timeout=10) as resp:
            return json.loads(resp.read())
    except (urllib.error.URLError, json.JSONDecodeError) as exc:
        raise TikhubError(f"{label} failed: {exc}") from exc


def health() -> dict:
    return _get_json(HEALTH_URL, "health check")


def platforms() -> Any:
    return _get_json(PLATFORMS_URL, "platforms check")

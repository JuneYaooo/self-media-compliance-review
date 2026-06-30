#!/usr/bin/env python3
"""Fetch and summarize optional Xiaohongshu dynamic evidence for compliance review."""

from __future__ import annotations

import argparse
import datetime as _dt
import json
import sys
from typing import Any

OFFICIAL_XHS_ACCOUNTS = {
    "规则百科薯",
    "薯管家",
    "商业合规薯",
    "健康薯",
    "好生意薯",
    "薯条小助手",
}

BASE_QUERIES = {
    "小红书": ["小红书 违规 申诉", "小红书 限流 怎么办", "小红书 小眼睛 不收录"],
    "抖音": ["抖音 违规 申诉 经验", "抖音 封号 解封 经验", "抖音 限流 怎么办 自救"],
}

RISK_QUERY_RULES = [
    (
        ("导流", "联系方式", "微信", "私信", "暗号", "群聊"),
        ["小红书 导流 违规 申诉", "小红书 评论 导流 暗号", "小红书 联系方式 怎么留 不违规"],
    ),
    (
        ("虚假营销", "伪素人", "不真诚", "带货", "软广"),
        ["小红书 虚假营销 处罚", "小红书 伪素人 违规", "小红书 不真诚营销推广"],
    ),
    (
        ("医疗", "医美", "功效", "减肥", "护肤", "保健"),
        ["小红书 医疗 功效 违规", "小红书 医美 违规 限流", "小红书 减肥 护肤 违禁词"],
    ),
    (
        ("搬运", "原创", "版权", "转载", "盗图"),
        ["小红书 搬运 原创 违规", "小红书 转载声明 怎么写", "小红书 盗图 抄袭 维权"],
    ),
    (("未成年", "儿童", "学生"), ["小红书 未成年 违规 处置"]),
    (("评论", "水军", "控评"), ["小红书 评论 控评 水军 违规"]),
    (("AI", "AIGC", "人工智能"), ["小红书 AI AIGC 标注", "小红书 AI 内容 违规"]),
    (("低浏览", "限流", "不收录", "小眼睛", "暗限流"), ["小红书 限流 小眼睛 不收录", "小红书 暗限流 申诉"]),
]


def _dedupe(values: list[str]) -> list[str]:
    seen = set()
    out = []
    for value in values:
        if value not in seen:
            seen.add(value)
            out.append(value)
    return out


def classify_author(nickname: str) -> str:
    return "官方治理账号" if nickname in OFFICIAL_XHS_ACCOUNTS else "创作者讨论样本"


def generate_queries(symptom: str, platform: str = "小红书", max_queries: int = 6) -> list[str]:
    text = f"{platform} {symptom}"
    queries: list[str] = []
    for needles, mapped_queries in RISK_QUERY_RULES:
        if any(needle in text for needle in needles):
            queries.extend(mapped_queries)
    queries.extend(BASE_QUERIES.get(platform, [f"{platform} 违规 申诉", f"{platform} 限流 怎么办"]))
    return _dedupe(queries)[:max_queries]


def _to_int(value: Any) -> int:
    try:
        return int(value)
    except (TypeError, ValueError):
        return 0


def _find_first(mapping: dict, keys: tuple[str, ...], default: Any = "") -> Any:
    for key in keys:
        value = mapping.get(key)
        if value not in (None, ""):
            return value
    return default


def _publish_time(card: dict) -> str:
    for item in (card.get("cornerTagInfo") or card.get("corner_tag_info") or []) or []:
        if isinstance(item, dict) and item.get("type") == "publish_time":
            return str(item.get("text", ""))
    return ""


def _search_items(payload: dict) -> list:
    data = payload.get("data") or {}
    nested = data.get("data") if isinstance(data, dict) else {}
    if isinstance(nested, dict):
        return nested.get("items") or []
    return []


def extract_notes(payload: dict, query: str) -> list[dict]:
    notes = []
    for item in _search_items(payload):
        if not isinstance(item, dict):
            continue
        card = item.get("noteCard") if isinstance(item.get("noteCard"), dict) else None
        if card is None:
            card = item.get("note") if isinstance(item.get("note"), dict) else {}
        user = card.get("user") if isinstance(card.get("user"), dict) else {}
        interact = card.get("interactInfo") if isinstance(card.get("interactInfo"), dict) else card
        author = str(_find_first(user, ("nickName", "nickname"), ""))
        notes.append(
            {
                "note_id": str(item.get("id") or card.get("id") or ""),
                "xsec_token": str(item.get("xsecToken") or card.get("xsec_token") or ""),
                "title": str(_find_first(card, ("displayTitle", "title", "desc"), "")),
                "author": author,
                "source_type": classify_author(author),
                "comment_count": _to_int(_find_first(interact, ("commentCount", "comment_count", "comments_count"), 0)),
                "like_count": _to_int(_find_first(interact, ("likedCount", "like_count", "liked_count"), 0)),
                "published_at": _publish_time(card),
                "query": query,
            }
        )
    return notes


def _comment_author(comment: dict) -> str:
    user = comment.get("user") or comment.get("user_info") or {}
    if isinstance(user, dict):
        return str(_find_first(user, ("nickname", "nickName"), ""))
    return ""


def extract_comments(payload: dict, note_id: str, max_comments: int = 20) -> list[dict]:
    raw_comments = (payload.get("data") or {}).get("comments") or []
    comments: list[dict] = []
    for comment in raw_comments:
        if not isinstance(comment, dict):
            continue
        comment_id = str(comment.get("id", ""))
        comments.append(
            {
                "note_id": note_id,
                "comment_id": comment_id,
                "parent_comment_id": "",
                "author": _comment_author(comment),
                "text": str(comment.get("content", "")).replace("\n", " ").strip(),
                "like_count": _to_int(comment.get("like_count")),
                "time": comment.get("time"),
            }
        )
        for reply in comment.get("sub_comments", []) or []:
            if isinstance(reply, dict):
                comments.append(
                    {
                        "note_id": note_id,
                        "comment_id": str(reply.get("id", "")),
                        "parent_comment_id": comment_id,
                        "author": _comment_author(reply),
                        "text": str(reply.get("content", "")).replace("\n", " ").strip(),
                        "like_count": _to_int(reply.get("like_count")),
                        "time": reply.get("time"),
                    }
                )
    comments = [comment for comment in comments if comment["text"]]
    comments.sort(key=lambda c: c["like_count"], reverse=True)
    return comments[:max_comments]


EVIDENCE_LIMITATION = "评论区讨论不是平台规则，只作为排查线索。"


def build_report(
    queries: list[str],
    notes: list[dict],
    comments: list[dict],
    sampled_at: str | None = None,
    errors: list[str] | None = None,
    warnings: list[str] | None = None,
) -> dict:
    return {
        "dynamic_search_enabled": not bool(errors),
        "sampled_at": sampled_at or _dt.date.today().isoformat(),
        "queries": queries,
        "notes": notes,
        "comments": comments,
        "warnings": warnings or [],
        "errors": errors or [],
        "evidence_limitation": EVIDENCE_LIMITATION,
    }


def _clip(text: str, limit: int = 90) -> str:
    return text if len(text) <= limit else text[: limit - 1] + "..."


def _table_cell(value: Any) -> str:
    return str(value).replace("|", "\\|").replace("\n", " ")


def render_markdown(report: dict) -> str:
    lines = [
        "## 动态小红书相似案例",
        "",
        f"- 状态: {'已启用' if report.get('dynamic_search_enabled') else '未启用'}",
        f"- 检索时间: {report.get('sampled_at', '')}",
        f"- 搜索词: {' / '.join(report.get('queries') or []) or '未检索'}",
        f"- 证据限制: {report.get('evidence_limitation', EVIDENCE_LIMITATION)}",
    ]
    if report.get("errors"):
        lines.append(f"- 未启用原因: {'; '.join(report['errors'])}")
    if report.get("warnings"):
        lines.append(f"- 注意: {'; '.join(report['warnings'])}")
    lines.extend(
        [
            "",
            "### 相关样本",
            "",
            "| 类型 | 作者 | note id | 标题 | 评论/点赞 |",
            "| --- | --- | --- | --- | --- |",
        ]
    )
    for note in report.get("notes", []):
        lines.append(
            f"| {_table_cell(note.get('source_type', ''))} | {_table_cell(note.get('author', ''))} | "
            f"{_table_cell(note.get('note_id', ''))} | {_table_cell(_clip(note.get('title', '')))} | "
            f"{note.get('comment_count', 0)}/{note.get('like_count', 0)} |"
        )
    if not report.get("notes"):
        lines.append("| 无 | 无 | 无 | 未取得动态样本 | 0/0 |")
    lines.extend(["", "### 高信号评论"])
    for comment in report.get("comments", [])[:8]:
        lines.append(
            f"- note `{comment.get('note_id', '')}` 👍{comment.get('like_count', 0)}: "
            f"{_clip(comment.get('text', ''), 120)}"
        )
    if not report.get("comments"):
        lines.append("- 未抓取到评论样本。")
    return "\n".join(lines) + "\n"


def run_search(client, query: str, max_notes: int = 8) -> list[dict]:
    try:
        payload = client.call("xiaohongshu_app_v2_search_notes", {"keyword": query, "page": 1})
    except Exception:
        payload = client.call("xiaohongshu_web_v3_fetch_search_notes", {"keyword": query, "page": 1})
    else:
        if isinstance(payload, dict) and payload.get("error"):
            payload = client.call("xiaohongshu_web_v3_fetch_search_notes", {"keyword": query, "page": 1})
    return extract_notes(payload, query)[:max_notes]


def run_comments(client, note_id: str, max_comments: int = 20) -> list[dict]:
    payload = client.call("xiaohongshu_web_v2_fetch_note_comments", {"note_id": note_id})
    return extract_comments(payload, note_id=note_id, max_comments=max_comments)


def run_diagnose(
    client,
    symptom: str,
    platform: str,
    max_notes: int = 8,
    max_comments: int = 8,
    comment_timeout: int = 15,
) -> dict:
    queries = generate_queries(symptom, platform=platform)
    notes: list[dict] = []
    warnings: list[str] = []
    seen_note_ids = set()
    for query in queries:
        for note in run_search(client, query, max_notes=max_notes):
            note_id = note.get("note_id")
            if note_id and note_id not in seen_note_ids:
                seen_note_ids.add(note_id)
                notes.append(note)
        if len(notes) >= max_notes:
            break
    notes = sorted(
        notes,
        key=lambda n: (
            n.get("source_type") != "官方治理账号",
            -n.get("comment_count", 0),
            -n.get("like_count", 0),
        ),
    )[:max_notes]
    comments: list[dict] = []
    if max_comments > 0:
        for note in notes[:3]:
            original_timeout = getattr(client, "timeout", None)
            if original_timeout is not None:
                client.timeout = min(original_timeout, comment_timeout)
            try:
                comments.extend(run_comments(client, note["note_id"], max_comments=max_comments))
            except Exception as exc:
                warnings.append(f"comments failed for {note['note_id']}: {exc}")
            finally:
                if original_timeout is not None:
                    client.timeout = original_timeout
    comments = sorted(comments, key=lambda c: -c.get("like_count", 0))[:max_comments]
    return build_report(queries, notes, comments, warnings=warnings)


def _load_tikhub_client_class():
    try:
        from tikhub.lib.tikhub_client import TikhubClient, TikhubError
    except ModuleNotFoundError:
        from tools.tikhub.lib.tikhub_client import TikhubClient, TikhubError
    return TikhubClient, TikhubError


def _print_json(report: dict) -> None:
    print(json.dumps(report, ensure_ascii=False, indent=2))


def _render(report: dict, output_format: str) -> None:
    if output_format == "json":
        _print_json(report)
    else:
        print(render_markdown(report), end="")


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Optional Xiaohongshu dynamic evidence search for compliance review.")
    subparsers = parser.add_subparsers(dest="command", required=True)

    common = argparse.ArgumentParser(add_help=False)
    common.add_argument("--format", choices=("markdown", "json"), default="markdown")

    search_parser = subparsers.add_parser("search", parents=[common], help="Search Xiaohongshu notes.")
    search_parser.add_argument("--query", required=True)
    search_parser.add_argument("--max-notes", type=int, default=8)

    comments_parser = subparsers.add_parser("comments", parents=[common], help="Fetch note comments.")
    comments_parser.add_argument("--note-id", required=True)
    comments_parser.add_argument("--max-comments", type=int, default=20)

    diagnose_parser = subparsers.add_parser("diagnose", parents=[common], help="Search similar XHS cases for a symptom.")
    diagnose_parser.add_argument("--symptom", required=True)
    diagnose_parser.add_argument("--platform", default="小红书")
    diagnose_parser.add_argument("--max-notes", type=int, default=8)
    diagnose_parser.add_argument("--max-comments", type=int, default=8)
    diagnose_parser.add_argument("--comment-timeout", type=int, default=15)

    args = parser.parse_args(argv)

    try:
        TikhubClient, _TikhubError = _load_tikhub_client_class()
        client = TikhubClient(platform="xiaohongshu")
        if args.command == "search":
            notes = run_search(client, args.query, max_notes=args.max_notes)
            report = build_report([args.query], notes, [])
        elif args.command == "comments":
            comments = run_comments(client, args.note_id, max_comments=args.max_comments)
            report = build_report([], [], comments)
        else:
            report = run_diagnose(
                client,
                symptom=args.symptom,
                platform=args.platform,
                max_notes=args.max_notes,
                max_comments=args.max_comments,
                comment_timeout=args.comment_timeout,
            )
    except Exception as exc:
        report = build_report([], [], [], errors=[str(exc)])

    _render(report, args.format)
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))

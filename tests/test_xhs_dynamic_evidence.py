import json
from pathlib import Path

import pytest

from tools.tikhub.lib import tikhub_client
from tools.tikhub.lib.tikhub_client import TikhubClient, TikhubError
from tools.xhs_dynamic_evidence import classify_author, generate_queries
from tools.xhs_dynamic_evidence import build_report, render_markdown
from tools.xhs_dynamic_evidence import extract_comments, extract_notes
from tools.xhs_dynamic_evidence import run_comments, run_diagnose, run_search


FIXTURES = Path(__file__).parent / "fixtures"


def load_fixture(name):
    return json.loads((FIXTURES / name).read_text())


def test_generate_queries_focuses_xhs_diversion_symptoms():
    queries = generate_queries("笔记被判导流，评论里留了暗号，申诉失败", platform="小红书")

    assert queries[0] == "小红书 导流 违规 申诉"
    assert "小红书 评论 导流 暗号" in queries
    assert "小红书 联系方式 怎么留 不违规" in queries
    assert len(queries) == len(set(queries))


def test_generate_queries_uses_xhs_as_cross_platform_discussion_venue():
    queries = generate_queries("抖音账号封号，想看有没有申诉经验", platform="抖音")

    assert "抖音 封号 解封 经验" in queries
    assert "抖音 违规 申诉 经验" in queries
    assert all("快手" not in q for q in queries)


def test_classify_author_marks_official_governance_accounts():
    assert classify_author("规则百科薯") == "官方治理账号"
    assert classify_author("商业合规薯") == "官方治理账号"
    assert classify_author("普通运营号") == "创作者讨论样本"


def test_extract_notes_from_web_v3_search_response():
    notes = extract_notes(load_fixture("xhs_search_notes.json"), query="小红书 导流 违规 申诉")

    assert notes[0]["note_id"] == "693bdcaf000000001e00ec5f"
    assert notes[0]["title"] == "「交易导流」违规整改指南"
    assert notes[0]["author"] == "规则百科薯"
    assert notes[0]["source_type"] == "官方治理账号"
    assert notes[0]["comment_count"] == 4408
    assert notes[0]["like_count"] == 6959
    assert notes[0]["published_at"] == "2025-12-15"
    assert notes[0]["query"] == "小红书 导流 违规 申诉"
    assert notes[1]["source_type"] == "创作者讨论样本"


def test_extract_notes_from_app_v2_search_response():
    notes = extract_notes(load_fixture("xhs_app_search_notes.json"), query="小红书 导流 违规 申诉")

    assert notes[0]["note_id"] == "63e3a1b6000000001d0121ff"
    assert notes[0]["title"] == "笔记玩法 | 笔记被限流？注意交易导流行为"
    assert notes[0]["author"] == "电商学习薯"
    assert notes[0]["comment_count"] == 800
    assert notes[0]["like_count"] == 2888
    assert notes[0]["published_at"] == "2023-02-11"


def test_extract_comments_keeps_nested_high_signal_replies():
    comments = extract_comments(load_fixture("xhs_note_comments.json"), note_id="693bdcaf000000001e00ec5f")

    assert comments[0]["comment_id"] == "c1"
    assert comments[0]["text"].startswith("麻烦平台把违规点写清楚")
    assert comments[0]["like_count"] == 2459
    assert comments[0]["author"] == "小北ybx"
    assert comments[0]["note_id"] == "693bdcaf000000001e00ec5f"
    assert comments[1]["comment_id"] == "c1-1"
    assert comments[1]["parent_comment_id"] == "c1"


def test_render_markdown_separates_dynamic_evidence_from_rules():
    notes = [
        {
            "note_id": "693bdcaf000000001e00ec5f",
            "title": "「交易导流」违规整改指南",
            "author": "规则百科薯",
            "source_type": "官方治理账号",
            "comment_count": 4408,
            "like_count": 6959,
            "published_at": "2025-12-15",
            "query": "小红书 导流 违规 申诉",
        }
    ]
    comments = [
        {
            "note_id": "693bdcaf000000001e00ec5f",
            "comment_id": "c1",
            "parent_comment_id": "",
            "author": "小北ybx",
            "text": "麻烦平台把违规点写清楚呀",
            "like_count": 2459,
            "time": 1765777293,
        }
    ]

    report = build_report(["小红书 导流 违规 申诉"], notes, comments, sampled_at="2026-06-30")
    markdown = render_markdown(report)

    assert report["dynamic_search_enabled"] is True
    assert "## 动态小红书相似案例" in markdown
    assert "检索时间: 2026-06-30" in markdown
    assert "评论区讨论不是平台规则，只作为排查线索" in markdown
    assert "693bdcaf000000001e00ec5f" in markdown
    assert "规则百科薯" in markdown
    assert "麻烦平台把违规点写清楚呀" in markdown


def test_render_markdown_escapes_table_pipes_in_note_titles():
    notes = [
        {
            "note_id": "63e3a1b6000000001d0121ff",
            "title": "笔记玩法 | 笔记被限流？注意交易导流行为",
            "author": "电商学习薯",
            "source_type": "创作者讨论样本",
            "comment_count": 800,
            "like_count": 2888,
        }
    ]

    markdown = render_markdown(build_report(["小红书 导流 违规 申诉"], notes, [], sampled_at="2026-06-30"))

    assert "笔记玩法 \\| 笔记被限流？注意交易导流行为" in markdown


def test_build_report_can_explain_disabled_dynamic_search():
    report = build_report([], [], [], sampled_at="2026-06-30", errors=["missing TIKHUB_API_KEY"])

    assert report["dynamic_search_enabled"] is False
    assert report["errors"] == ["missing TIKHUB_API_KEY"]


class FakeClient:
    def __init__(self):
        self.calls = []

    def call(self, tool_name, arguments):
        self.calls.append((tool_name, arguments))
        if tool_name == "xiaohongshu_app_v2_search_notes":
            return load_fixture("xhs_app_search_notes.json")
        if tool_name == "xiaohongshu_web_v3_fetch_search_notes":
            return load_fixture("xhs_search_notes.json")
        if tool_name == "xiaohongshu_web_v2_fetch_note_comments":
            return load_fixture("xhs_note_comments.json")
        raise AssertionError(tool_name)


class FallbackClient:
    def __init__(self):
        self.calls = []

    def call(self, tool_name, arguments):
        self.calls.append((tool_name, arguments))
        if tool_name == "xiaohongshu_app_v2_search_notes":
            return {"error": "RetryError[<HTTPStatusError>]"}
        if tool_name == "xiaohongshu_web_v3_fetch_search_notes":
            return load_fixture("xhs_search_notes.json")
        raise AssertionError(tool_name)


class ExceptionFallbackClient:
    def __init__(self):
        self.calls = []

    def call(self, tool_name, arguments):
        self.calls.append((tool_name, arguments))
        if tool_name == "xiaohongshu_app_v2_search_notes":
            raise RuntimeError("app search timed out")
        if tool_name == "xiaohongshu_web_v3_fetch_search_notes":
            return load_fixture("xhs_search_notes.json")
        raise AssertionError(tool_name)


class CommentFailureClient:
    def __init__(self):
        self.calls = []
        self.timeout = 60

    def call(self, tool_name, arguments):
        self.calls.append((tool_name, arguments, self.timeout))
        if tool_name == "xiaohongshu_app_v2_search_notes":
            return load_fixture("xhs_app_search_notes.json")
        if tool_name == "xiaohongshu_web_v3_fetch_search_notes":
            return load_fixture("xhs_search_notes.json")
        if tool_name == "xiaohongshu_web_v2_fetch_note_comments":
            raise RuntimeError("comment endpoint timed out")
        raise AssertionError(tool_name)


def test_run_search_uses_xhs_app_v2_search_tool_first():
    client = FakeClient()
    notes = run_search(client, "小红书 导流 违规 申诉", max_notes=1)

    assert client.calls[0] == (
        "xiaohongshu_app_v2_search_notes",
        {"keyword": "小红书 导流 违规 申诉", "page": 1},
    )
    assert len(notes) == 1


def test_run_search_falls_back_to_web_v3_when_app_v2_returns_error_payload():
    client = FallbackClient()
    notes = run_search(client, "小红书 导流 违规 申诉", max_notes=1)

    assert client.calls == [
        ("xiaohongshu_app_v2_search_notes", {"keyword": "小红书 导流 违规 申诉", "page": 1}),
        ("xiaohongshu_web_v3_fetch_search_notes", {"keyword": "小红书 导流 违规 申诉", "page": 1}),
    ]
    assert notes[0]["note_id"] == "693bdcaf000000001e00ec5f"


def test_run_search_falls_back_to_web_v3_when_app_v2_raises():
    client = ExceptionFallbackClient()
    notes = run_search(client, "小红书 导流 违规 申诉", max_notes=1)

    assert client.calls == [
        ("xiaohongshu_app_v2_search_notes", {"keyword": "小红书 导流 违规 申诉", "page": 1}),
        ("xiaohongshu_web_v3_fetch_search_notes", {"keyword": "小红书 导流 违规 申诉", "page": 1}),
    ]
    assert notes[0]["note_id"] == "693bdcaf000000001e00ec5f"


def test_run_comments_uses_web_v2_comments_without_xsec_token():
    client = FakeClient()
    comments = run_comments(client, "693bdcaf000000001e00ec5f", max_comments=1)

    assert client.calls[0] == (
        "xiaohongshu_web_v2_fetch_note_comments",
        {"note_id": "693bdcaf000000001e00ec5f"},
    )
    assert len(comments) == 1


def test_run_diagnose_combines_queries_notes_and_comments():
    client = FakeClient()
    report = run_diagnose(client, "笔记被判导流，申诉失败", "小红书", max_notes=1, max_comments=1)

    assert report["dynamic_search_enabled"] is True
    assert report["queries"][0] == "小红书 导流 违规 申诉"
    assert report["notes"][0]["note_id"] == "63e3a1b6000000001d0121ff"
    assert report["comments"][0]["note_id"] == "63e3a1b6000000001d0121ff"


def test_run_diagnose_keeps_notes_and_warns_when_comments_fail():
    client = CommentFailureClient()
    report = run_diagnose(client, "笔记被判导流，申诉失败", "小红书", max_notes=1, max_comments=1, comment_timeout=15)

    assert report["dynamic_search_enabled"] is True
    assert report["notes"][0]["note_id"] == "63e3a1b6000000001d0121ff"
    assert report["comments"] == []
    assert "comments failed for 63e3a1b6000000001d0121ff: comment endpoint timed out" in report["warnings"]
    assert client.calls[-1][2] == 15
    assert client.timeout == 60


def test_docs_describe_dynamic_search_as_optional_and_xhs_only():
    skill = Path("skills/self-media-compliance-review/SKILL.md").read_text()
    readme = Path("README.md").read_text()
    sources = Path("docs/sources.md").read_text()

    assert "动态小红书相似案例" in skill
    assert "可选增强" in skill
    assert "未配置 `TIKHUB_API_KEY`" in skill
    assert "只通过小红书" in readme
    assert "tools/xhs_dynamic_evidence.py diagnose" in readme
    assert "TikHub" in sources
    assert "评论区讨论不是平台规则" in sources


def test_tikhub_client_wraps_socket_timeout_as_tikhub_error(monkeypatch):
    def raise_timeout(*_args, **_kwargs):
        raise TimeoutError("read timed out")

    monkeypatch.setattr(tikhub_client.urllib.request, "urlopen", raise_timeout)
    client = TikhubClient("xiaohongshu", api_key="fake-key", timeout=1)

    with pytest.raises(TikhubError, match="network timeout"):
        client._post({"jsonrpc": "2.0", "id": 1, "method": "tools/call", "params": {}}, session_id=None)

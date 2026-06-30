from pathlib import Path


def test_single_skill_repository_uses_root_level_layout():
    assert Path("SKILL.md").is_file()
    assert Path("agents/openai.yaml").is_file()
    assert Path("references/xiaohongshu.md").is_file()
    assert Path("references/cases/xiaohongshu.md").is_file()
    assert not Path("skills/self-media-compliance-review/SKILL.md").exists()


def test_docs_link_to_root_level_skill_layout():
    readme = Path("README.md").read_text()
    sources = Path("docs/sources.md").read_text()

    assert "./SKILL.md" in readme
    assert "./references/xiaohongshu.md" in readme
    assert "./references/cases/xiaohongshu.md" in readme
    assert "./references/recent-cases-2025-2026.md" in readme
    assert "references/cases/xiaohongshu.md" in sources
    assert "skills/self-media-compliance-review" not in readme
    assert "skills/self-media-compliance-review" not in sources

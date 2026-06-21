#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
SKILL_DIR="$ROOT_DIR/skills/self-media-compliance-review"
VALIDATOR="${SKILL_VALIDATOR:-$HOME/.codex/skills/.system/skill-creator/scripts/quick_validate.py}"

if [[ -f "$VALIDATOR" ]]; then
  python3 "$VALIDATOR" "$SKILL_DIR"
else
  echo "Skill validator not found at $VALIDATOR; running repository-local checks."
  python3 - "$SKILL_DIR/SKILL.md" <<'PY'
from pathlib import Path
import re
import sys

path = Path(sys.argv[1])
text = path.read_text(encoding="utf-8")
if not text.startswith("---\n"):
    raise SystemExit("SKILL.md missing YAML frontmatter")
end = text.find("\n---\n", 4)
if end == -1:
    raise SystemExit("SKILL.md frontmatter is not closed")
frontmatter = text[4:end]
for key in ("name", "description"):
    if not re.search(rf"^{key}:\s*.+$", frontmatter, re.M):
        raise SystemExit(f"SKILL.md missing frontmatter field: {key}")
name = re.search(r"^name:\s*(.+)$", frontmatter, re.M).group(1).strip().strip('"')
if not re.fullmatch(r"[A-Za-z0-9-]+", name):
    raise SystemExit("SKILL.md name must contain only letters, numbers, and hyphens")
PY
fi

required_files=(
  "$SKILL_DIR/SKILL.md"
  "$SKILL_DIR/agents/openai.yaml"
  "$SKILL_DIR/references/wechat-channels.md"
  "$SKILL_DIR/references/wechat-official-account.md"
  "$SKILL_DIR/references/douyin.md"
  "$SKILL_DIR/references/kuaishou.md"
  "$SKILL_DIR/references/bilibili.md"
  "$SKILL_DIR/references/xiaohongshu.md"
  "$SKILL_DIR/references/recent-cases-2025-2026.md"
  "$SKILL_DIR/references/cases/xiaohongshu.md"
  "$SKILL_DIR/references/cases/wechat-official-account.md"
  "$SKILL_DIR/references/cases/wechat-channels.md"
  "$SKILL_DIR/references/cases/douyin.md"
  "$SKILL_DIR/references/cases/kuaishou.md"
  "$SKILL_DIR/references/cases/bilibili.md"
  "$ROOT_DIR/docs/sources.md"
)

for file in "${required_files[@]}"; do
  if [[ ! -f "$file" ]]; then
    echo "Missing required file: $file" >&2
    exit 1
  fi
done

for ref in wechat-channels wechat-official-account douyin kuaishou bilibili xiaohongshu; do
  if ! grep -q "references/$ref.md" "$SKILL_DIR/SKILL.md"; then
    echo "SKILL.md does not route to references/$ref.md" >&2
    exit 1
  fi
done

if ! grep -q "references/recent-cases-2025-2026.md" "$SKILL_DIR/SKILL.md"; then
  echo "SKILL.md does not route to references/recent-cases-2025-2026.md" >&2
  exit 1
fi

for case_ref in xiaohongshu wechat-official-account wechat-channels douyin kuaishou bilibili; do
  if ! grep -q "references/cases/$case_ref.md" "$SKILL_DIR/SKILL.md"; then
    echo "SKILL.md does not route to references/cases/$case_ref.md" >&2
    exit 1
  fi
  if ! grep -q "cases/$case_ref.md" "$SKILL_DIR/references/recent-cases-2025-2026.md"; then
    echo "recent-cases-2025-2026.md does not route to cases/$case_ref.md" >&2
    exit 1
  fi
  if ! grep -q "Scenario Playbooks" "$SKILL_DIR/references/cases/$case_ref.md"; then
    echo "cases/$case_ref.md does not include Scenario Playbooks" >&2
    exit 1
  fi
done

if grep -RInE 'TODO|\[TODO|placeholder' "$SKILL_DIR" "$ROOT_DIR/docs"; then
  echo "Found placeholder text" >&2
  exit 1
fi

for platform in "WeChat Official Accounts" Douyin Kuaishou Bilibili Xiaohongshu; do
  if ! grep -q "$platform" "$ROOT_DIR/docs/sources.md"; then
    echo "Missing source section for $platform" >&2
    exit 1
  fi
done

echo "Validation passed."

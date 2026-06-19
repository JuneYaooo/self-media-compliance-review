#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
SKILL_DIR="$ROOT_DIR/skills/self-media-compliance-review"
VALIDATOR="${SKILL_VALIDATOR:-$HOME/.codex/skills/.system/skill-creator/scripts/quick_validate.py}"

if [[ ! -f "$VALIDATOR" ]]; then
  echo "Missing skill validator: $VALIDATOR" >&2
  exit 1
fi

python3 "$VALIDATOR" "$SKILL_DIR"

required_files=(
  "$SKILL_DIR/SKILL.md"
  "$SKILL_DIR/agents/openai.yaml"
  "$SKILL_DIR/references/wechat-channels.md"
  "$SKILL_DIR/references/douyin.md"
  "$SKILL_DIR/references/bilibili.md"
  "$SKILL_DIR/references/xiaohongshu.md"
  "$ROOT_DIR/docs/sources.md"
)

for file in "${required_files[@]}"; do
  if [[ ! -f "$file" ]]; then
    echo "Missing required file: $file" >&2
    exit 1
  fi
done

for ref in wechat-channels douyin bilibili xiaohongshu; do
  if ! grep -q "references/$ref.md" "$SKILL_DIR/SKILL.md"; then
    echo "SKILL.md does not route to references/$ref.md" >&2
    exit 1
  fi
done

if grep -RInE 'TODO|\[TODO|placeholder' "$SKILL_DIR" "$ROOT_DIR/docs"; then
  echo "Found placeholder text" >&2
  exit 1
fi

for platform in Douyin Bilibili Xiaohongshu; do
  if ! grep -q "$platform" "$ROOT_DIR/docs/sources.md"; then
    echo "Missing source section for $platform" >&2
    exit 1
  fi
done

echo "Validation passed."

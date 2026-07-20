#!/usr/bin/env bash
# 将源仓库中的 fun-title-generator skill 同步到 kigland-media 的 .cursor/skills/ 使用处拷贝。
# 用法：在本仓库任意位置运行 scripts/sync-to-cursor.sh
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
SRC="$SCRIPT_DIR/../skills/fun-title-generator/"
DEST="$SCRIPT_DIR/../../.cursor/skills/fun-title-generator/"

if [[ ! -d "$SRC" ]]; then
  echo "ERROR: 源目录不存在: $SRC" >&2
  exit 1
fi

mkdir -p "$DEST"

echo "同步: $SRC"
echo "  ->: $DEST"
rsync -a --delete "$SRC" "$DEST"

echo "验证两份拷贝是否一致 (diff -rq)..."
if diff -rq "$SRC" "$DEST"; then
  echo "OK: 两份拷贝完全一致。"
else
  echo "ERROR: 同步后仍存在差异，请检查上方输出。" >&2
  exit 1
fi

#!/usr/bin/env bash
#
# package.sh — build upload-ready .zip archives from the canonical skill folders.
#
# Claude's web and desktop apps (and the Skills API) take a skill as a zip whose
# root is the skill folder itself:  flux-v2.zip -> flux-v2/SKILL.md
#
# Usage: scripts/package.sh [<skill>...|--all]   ->  dist/<skill>.zip

set -euo pipefail

REPO_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd -P)"
DIST="$REPO_ROOT/dist"

ALL=0
SKILLS=()

usage() {
  cat <<'EOF'
Usage: scripts/package.sh [<skill>...|--all]

Builds dist/<skill>.zip for each named skill, laid out the way claude.ai and the
Skills API expect (the skill folder at the root of the archive).

Options:
  --all         package every skill in the repo
  --list        print packageable skill names and exit
  -h, --help    this message

Upload the result at:  Claude -> Settings -> Capabilities -> Skills -> Add
EOF
}

discover() {
  {
    find "$REPO_ROOT/skills" -mindepth 2 -maxdepth 2 2>/dev/null || true
    find "$REPO_ROOT/.claude/skills" -mindepth 1 -maxdepth 1 2>/dev/null || true
  } | while IFS= read -r d; do
      [ -d "$d" ] && [ -f "$d/SKILL.md" ] || continue
      real="$(cd "$d" && pwd -P)"
      printf '%s\t%s\n' "$(basename "$real")" "$real"
    done | awk -F'\t' '!seen[$2]++' | sort
}

while [ $# -gt 0 ]; do
  case "$1" in
    --all)      ALL=1 ;;
    --list)     discover | cut -f1; exit 0 ;;
    -h|--help)  usage; exit 0 ;;
    -*)         echo "Unknown option: $1" >&2; usage >&2; exit 2 ;;
    *)          SKILLS+=("$1") ;;
  esac
  shift
done

command -v zip >/dev/null 2>&1 || { echo "zip is not installed." >&2; exit 1; }

CATALOG="$(discover)"

if [ "$ALL" -eq 0 ] && [ ${#SKILLS[@]} -eq 0 ]; then
  echo "Nothing to package. Name a skill, or pass --all." >&2
  usage >&2
  exit 2
fi

selected=""
if [ "$ALL" -eq 1 ]; then
  selected="$CATALOG"
else
  for want in "${SKILLS[@]}"; do
    match="$(printf '%s\n' "$CATALOG" | awk -F'\t' -v n="$want" '$1 == n')"
    if [ -z "$match" ]; then
      echo "No skill named '$want'." >&2
      echo "Available:" >&2
      printf '%s\n' "$CATALOG" | cut -f1 | sed 's/^/  /' >&2
      exit 1
    fi
    selected="${selected}${match}
"
  done
  selected="$(printf '%s' "$selected" | sed '/^$/d')"
fi

mkdir -p "$DIST"

printf '%s\n' "$selected" | while IFS="$(printf '\t')" read -r name src; do
  [ -n "$name" ] || continue
  rm -f "$DIST/$name.zip"
  # Zip from the skill's parent so the folder itself is the archive root.
  (cd "$(dirname "$src")" && zip -q -r -X "$DIST/$name.zip" "$name" -x '*.DS_Store' '*/__MACOSX/*')
  printf '  %s -> dist/%s.zip\n' "$name" "$name"
done

echo
echo "Done. Archives in: $DIST"

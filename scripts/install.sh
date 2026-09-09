#!/usr/bin/env bash
#
# install.sh — install super-skills into any tool that reads the SKILL.md format.
#
# A skill is a folder containing SKILL.md. Claude Code and Codex only discover
# skills ONE LEVEL DEEP, so the category dirs (skills/image, skills/video) cannot
# be copied wholesale — this script flattens them into the target skills dir.
#
# Usage: scripts/install.sh [<skill>...] [options]
# Run with --help for the full option list.

set -euo pipefail

REPO_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd -P)"

TARGET=""
MODE="copy"
ALL=0
FORCE=0
DRY_RUN=0
LIST=0
SKILLS=()

usage() {
  cat <<'EOF'
Usage: scripts/install.sh [<skill>...] [options]

Installs one or more skills into a tool's skills directory. Each skill lands as
a single flat folder (<target>/<skill>/SKILL.md) because Claude Code and Codex
only look one level deep.

Targets (pick one; default --claude-code):
  --claude-code           ~/.claude/skills/        Claude Code, every project
  --claude-code-project   ./.claude/skills/        Claude Code, this repo only
  --cursor                ~/.cursor/skills/        Cursor, every project
  --cursor-project        ./.cursor/skills/        Cursor, this repo only
  --codex                 ~/.agents/skills/        Codex, user level
  --codex-project         ./.agents/skills/        Codex, repo level
  --target <dir>          anywhere else

Options:
  --all                   install every skill in the repo
  --link                  symlink instead of copy (relative symlinks)
  --force                 replace an existing entry
  --list                  print installable skill names and exit
  --dry-run               show what would happen, change nothing
  -h, --help              this message

Examples:
  scripts/install.sh veo-v3                       # one skill, user-level Claude Code
  scripts/install.sh --all --cursor               # everything, into Cursor
  scripts/install.sh flux-v2 --target ~/somewhere
  scripts/install.sh --all --claude-code-project --link   # dev setup for this repo
EOF
}

# Print "<name><TAB><absolute real path>" for every skill in the repo, deduped by
# real path so the .claude/skills symlinks don't show up twice.
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

# relpath <target-abs> <base-dir-abs> — path to reach target from inside base
relpath() {
  local target="$1" base="$2" up=""
  while [ "${target#"$base"/}" = "$target" ]; do
    [ "$base" = "/" ] && { printf '%s\n' "$target"; return; }
    base="$(dirname "$base")"
    up="../$up"
  done
  printf '%s%s\n' "$up" "${target#"$base"/}"
}

while [ $# -gt 0 ]; do
  case "$1" in
    --claude-code)          TARGET="$HOME/.claude/skills" ;;
    --claude-code-project)  TARGET="$REPO_ROOT/.claude/skills" ;;
    --cursor)               TARGET="$HOME/.cursor/skills" ;;
    --cursor-project)       TARGET="$REPO_ROOT/.cursor/skills" ;;
    --codex)                TARGET="$HOME/.agents/skills" ;;
    --codex-project)        TARGET="$REPO_ROOT/.agents/skills" ;;
    --target)               shift; [ $# -gt 0 ] || { echo "--target needs a directory" >&2; exit 2; }; TARGET="$1" ;;
    --all)                  ALL=1 ;;
    --link)                 MODE="link" ;;
    --force)                FORCE=1 ;;
    --list)                 LIST=1 ;;
    --dry-run)              DRY_RUN=1 ;;
    -h|--help)              usage; exit 0 ;;
    -*)                     echo "Unknown option: $1" >&2; usage >&2; exit 2 ;;
    *)                      SKILLS+=("$1") ;;
  esac
  shift
done

CATALOG="$(discover)"

if [ "$LIST" -eq 1 ]; then
  printf '%s\n' "$CATALOG" | while IFS="$(printf '\t')" read -r name path; do
    printf '%-26s %s\n' "$name" "${path#"$REPO_ROOT"/}"
  done
  exit 0
fi

if [ "$ALL" -eq 0 ] && [ ${#SKILLS[@]} -eq 0 ]; then
  echo "Nothing to install. Name a skill, or pass --all. Try --list to see what's here." >&2
  usage >&2
  exit 2
fi

[ -n "$TARGET" ] || TARGET="$HOME/.claude/skills"

# Resolve requested names to paths.
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

if [ "$DRY_RUN" -eq 0 ]; then
  mkdir -p "$TARGET"
fi
TARGET_ABS="$(cd "$TARGET" 2>/dev/null && pwd -P || printf '%s' "$TARGET")"


printf '%s\n' "$selected" | while IFS="$(printf '\t')" read -r name src; do
  [ -n "$name" ] || continue
  dest="$TARGET_ABS/$name"

  # Already the canonical home for this skill (e.g. the dev skills when
  # installing into this repo's own .claude/skills).
  if [ "$src" = "$dest" ]; then
    echo "  = $name (already in place)"
    continue
  fi

  if [ -e "$dest" ] || [ -L "$dest" ]; then
    if [ "$FORCE" -eq 1 ]; then
      [ "$DRY_RUN" -eq 1 ] || rm -rf "$dest"
    else
      echo "  ! $name exists — skipping (use --force to replace)"
      continue
    fi
  fi

  if [ "$MODE" = "link" ]; then
    link="$(relpath "$src" "$TARGET_ABS")"
    echo "  → $name -> $link"
    [ "$DRY_RUN" -eq 1 ] || ln -s "$link" "$dest"
  else
    echo "  + $name"
    if [ "$DRY_RUN" -eq 0 ]; then
      mkdir -p "$dest"
      (cd "$src" && tar -cf - --exclude '.DS_Store' .) | (cd "$dest" && tar -xf -)
    fi
  fi
done

echo
if [ "$DRY_RUN" -eq 1 ]; then
  echo "Dry run — nothing written. Target would be: $TARGET_ABS"
else
  echo "Done. Target: $TARGET_ABS"
fi

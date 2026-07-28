#!/bin/bash
# Build/package/install for the-style-guide.
set -euo pipefail

SKILL_NAME="the-style-guide"
ROOT="$(cd "$(dirname "$0")" && pwd)"
SRC="$ROOT/src/$SKILL_NAME"
TARGET_DIR="$ROOT/target"
TARGET="$TARGET_DIR/$SKILL_NAME"
ZIP="$TARGET_DIR/$SKILL_NAME.zip"
DIST_DIR="$ROOT/dist"
DIST_ZIP="$DIST_DIR/$SKILL_NAME.zip"
SBOM="$DIST_DIR/$SKILL_NAME.cdx.json"
DEST_ROOT="${SKILL_INSTALL_DIR:-$HOME/.claude/skills}"
DEST="$DEST_ROOT/$SKILL_NAME"

usage() {
    cat <<USAGE
Usage: ./build.sh [flags]

Build $SKILL_NAME skill. Flags are opt-in and combinable.

Flags:
  --install      Build, zip, and copy into \$SKILL_INSTALL_DIR
                 (default: ~/.claude/skills/). Makes the skill
                 immediately discoverable by Claude Code.
  --package      Build, zip, copy to dist/$SKILL_NAME.zip, and
                 emit a CycloneDX SBOM at dist/$SKILL_NAME.cdx.json.
                 Tracked release artifacts.
  -h, --help     Show this help and exit.

Examples:
  ./build.sh --install                Local dev install.
  ./build.sh --package                Refresh the committed release artifacts.
  ./build.sh --install --package      Both.

See README.md for the release process.
USAGE
}

INSTALL=false
PACKAGE=false

if [[ $# -eq 0 ]]; then
    usage; exit 0
fi

for arg in "$@"; do
    case "$arg" in
        --install)    INSTALL=true ;;
        --package)    PACKAGE=true ;;
        -h|--help)    usage; exit 0 ;;
        *) echo "Unknown flag: $arg" >&2; echo; usage; exit 2 ;;
    esac
done

[[ -d "$SRC" ]] || { echo "Error: $SRC missing" >&2; exit 1; }

rm -rf "$TARGET" "$ZIP"
mkdir -p "$TARGET_DIR"
cp -R "$SRC" "$TARGET"

find "$TARGET" \( -name '.DS_Store' -o -name '._*' \) -delete 2>/dev/null || true

if [[ -d "$TARGET/scripts" ]]; then
    find "$TARGET/scripts" -type f -exec chmod u+x {} \;
fi

(cd "$TARGET_DIR" && zip -qr "$SKILL_NAME.zip" "$SKILL_NAME")

echo "Built:  $TARGET"
echo "Zipped: $ZIP"

if $PACKAGE; then
    mkdir -p "$DIST_DIR"
    cp "$ZIP" "$DIST_ZIP"
    echo "Packaged: $DIST_ZIP"

    ZIP_SHA="$(shasum -a 256 "$DIST_ZIP" | awk '{print $1}')"
    TS="$(date -u +%Y-%m-%dT%H:%M:%SZ)"
    UUID="$(uuidgen | tr 'A-Z' 'a-z')"
    cat > "$SBOM" <<EOF
{
  "bomFormat": "CycloneDX",
  "specVersion": "1.6",
  "serialNumber": "urn:uuid:$UUID",
  "version": 1,
  "metadata": {
    "timestamp": "$TS",
    "tools": [
      { "vendor": "the-skill-builder", "name": "build.sh", "version": "1.0" }
    ],
    "component": {
      "type": "application",
      "bom-ref": "pkg:generic/$SKILL_NAME@1.6",
      "name": "$SKILL_NAME",
      "version": "1.6",
      "description": "A portable multi-style guide for writing and question-asking, holding named voices (Coté prose, Tyler Cowen questions, LinkedIn) and shared references.",
      "licenses": [ { "license": { "id": "CC0-1.0" } } ],
      "authors": [ { "name": "Coté" } ],
      "hashes": [ { "alg": "SHA-256", "content": "$ZIP_SHA" } ]
    }
  },
  "components": []
}
EOF
    echo "SBOM:     $SBOM"
fi

if $INSTALL; then
    mkdir -p "$DEST_ROOT"
    rm -rf "$DEST"
    cp -R "$TARGET" "$DEST"
    echo "Installed: $DEST"
fi

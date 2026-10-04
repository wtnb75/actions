#!/usr/bin/env bash
# Helper for the *update actions: build a PR body listing updated dependencies.
#
#   dep-diff.sh snapshot <go|node|toml|pub> [lockfile]   -> "<name> <version>" lines on stdout
#   dep-diff.sh diff <before> <after> [title]            -> markdown on stdout
#
# kinds: go   = `go list -m all` (lockfile is ignored)
#        node = pnpm-lock.yaml
#        toml = uv.lock / Cargo.lock ([[package]] name/version)
#        pub  = pubspec.lock
set -euo pipefail

snapshot() {
  local kind=$1 file=${2:-}
  # a missing lockfile (e.g. a library crate without Cargo.lock) is treated as empty
  if [ "$kind" != go ] && [ ! -f "$file" ]; then
    return 0
  fi
  case "$kind" in
  go)
    go list -m all | awk 'NR > 1 && $2 != "" { print $1, $2 }'
    ;;
  node)
    awk '
      /^[A-Za-z]/ { in_pkgs = ($0 == "packages:"); next }
      in_pkgs && match($0, /^  [^ ].*:$/) {
        key = substr($0, 3, length($0) - 3)
        gsub(/'\''/, "", key)
        sub(/^\//, "", key)
        sub(/\(.*$/, "", key)
        at = match(key, /@[^@]*$/)
        if (at > 1) print substr(key, 1, at - 1), substr(key, at + 1)
      }' "$file"
    ;;
  toml)
    awk '
      /^\[\[package\]\]/ { name = ""; next }
      /^name = / { gsub(/^name = "|"$/, ""); name = $0; next }
      /^version = / && name != "" { gsub(/^version = "|"$/, ""); print name, $0; name = "" }
    ' "$file"
    ;;
  pub)
    awk '
      /^[a-z]/ { in_pkgs = ($0 == "packages:"); next }
      in_pkgs && /^  [A-Za-z0-9_]+:$/ { name = $1; sub(/:$/, "", name); next }
      in_pkgs && /^    version: / { gsub(/^    version: "|"$/, ""); print name, $0 }
    ' "$file"
    ;;
  *)
    echo "unknown kind: $kind" >&2
    exit 2
    ;;
  esac | LC_ALL=C sort -u
}

diff_snapshots() {
  local before=$1 after=$2 title=${3:-Dependency updates}
  local rows
  [ -f "$before" ] && [ -f "$after" ] || {
    echo "snapshot file missing: $before / $after" >&2
    return 1
  }
  # nothing parsed on either side: do not claim "no changes", the parser may be out of date
  if [ ! -s "$before" ] && [ ! -s "$after" ]; then
    fallback "$title"
    return
  fi
  rows=$(awk '
    FNR == NR { b[$1] = ($1 in b) ? b[$1] ", " $2 : $2; names[$1] = 1; next }
    { a[$1] = ($1 in a) ? a[$1] ", " $2 : $2; names[$1] = 1 }
    END {
      for (n in names) {
        bv = (n in b) ? b[n] : "-"
        av = (n in a) ? a[n] : "-"
        if (bv != av) printf "| %s | %s | %s |\n", n, bv, av
      }
    }' "$before" "$after" | LC_ALL=C sort)
  echo "## $title"
  echo
  if [ -z "$rows" ]; then
    echo "No dependency version changes detected."
    return
  fi
  echo "$(printf '%s\n' "$rows" | wc -l | tr -d ' ') package(s) changed."
  echo
  echo "| Package | Before | After |"
  echo "| --- | --- | --- |"
  printf '%s\n' "$rows"
}

# body used when the changes could not be determined
fallback() {
  echo "## ${1:-Dependency updates}"
  echo
  echo "The list of changed packages could not be generated automatically."
  echo "Please check the file changes in this PR."
}

case "${1:-}" in
snapshot) shift; snapshot "$@" ;;
diff) shift; diff_snapshots "$@" ;;
fallback) shift; fallback "$@" ;;
*)
  echo "usage: $0 snapshot <go|node|toml|pub> [lockfile] | diff <before> <after> [title] | fallback [title]" >&2
  exit 2
  ;;
esac

#! /bin/sh
# Usage: $0 ../*/action.yml
set -x
d=$(dirname $0)

for i; do
  [ -f $i ] || continue
  dn=$(dirname $i)
  fn=$(basename $dn)
  jinja -D filename $fn -d $i -f yaml $d/readme.j2 -o $dn/README.md
  # jinja2 -D filename=$fn readme.j2 $i --format yaml -o $dn/README.md
done

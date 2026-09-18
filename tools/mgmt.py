import click
import requests
import subprocess
import re
import functools
from natsort import natsorted
from logging import getLogger

_log = getLogger(__name__)


@click.group(invoke_without_command=True)
@click.pass_context
@click.version_option(version="0.1", prog_name="mgmt")
def cli(ctx):
    if ctx.invoked_subcommand is None:
        print(ctx.get_help())


def set_verbose(flag):
    from logging import basicConfig, DEBUG, INFO, WARNING
    fmt = '%(asctime)s %(levelname)s %(message)s'
    print("flag=%s" %flag)
    if flag is None:
        basicConfig(level=INFO, format=fmt)
    elif flag:
        basicConfig(level=DEBUG, format=fmt)
    else:
        basicConfig(level=WARNING, format=fmt)


def common_option(func):
    @click.option("--verbose/--quiet", default=None)
    @functools.wraps(func)
    def _(verbose, *args, **kwargs):
        set_verbose(verbose)
        return func(*args, **kwargs)
    return _


class VersionCheck:
    # matches a `uses:` line, capturing the referenced action and an
    # optional trailing `# vX.Y.Z` comment. YAML parsing drops comments,
    # and this repo pins actions by commit SHA with the human-readable
    # version recorded only in that comment, so `uses:` lines are read
    # as raw text instead of via a YAML loader.
    uses_line_regexp = re.compile(
        r"^\s*(?:-\s*)?uses:\s*(?P<uses>\S+)\s*(?:#\s*(?P<comment>\S+))?\s*$")
    action_regexp = re.compile(
        r"^(?P<org>[a-zA-Z0-9_-]+)/(?P<repo>[a-zA-Z0-9_.-]+)@(?P<ref>[0-9a-f]{40}|v[0-9]+(?:\.[0-9]+){0,2})$")
    sha_regexp = re.compile(r"^[0-9a-f]{40}$")
    version_regexp = re.compile(r"^v[0-9]+(?:\.[0-9]+){0,2}$")

    def get_newest(self, val: list[str]) -> str:
        _log.debug("choose newest: %s", val)
        vers = [x for x in val if self.version_regexp.match(x)]
        if not vers:
            return None
        # prefer the most specific tag shape (e.g. v1.2.3 over a
        # coexisting moving v1 alias) before sorting naturally
        max_parts = max(v.count(".") for v in vers)
        vers = natsorted(v for v in vers if v.count(".") == max_parts)
        _log.debug("sorted: %s", vers)
        return vers[-1]

    @functools.cache
    def get_version_git_tag(self, url):
        tags = []
        for line in subprocess.check_output(["git", "ls-remote", "--tags", url], text=True).splitlines():
            v = line.strip().split()
            tagstr = v[-1].split("/", 2)[-1]
            if tagstr.endswith("{}"):
                continue
            tags.append(tagstr)
        return self.get_newest(tags)

    def get_version_github_release(self, id):
        res = requests.get(
            f"https://api.github.com/repos/{id}/releases/latest").json()
        return self.get_newest([res.get("tag_name")])

    def get_version_github_tag(self, id):
        return self.get_version_git_tag(url=f"https://github.com/{id}")

    def check_version(self, filename, text) -> list[dict]:
        _log.info("start check %s", filename)
        res = []
        for lineno, line in enumerate(text.splitlines(), start=1):
            m = self.uses_line_regexp.match(line)
            if not m:
                continue
            m2 = self.action_regexp.match(m.group("uses"))
            if not m2:
                continue
            org = m2.group("org")
            repo = m2.group("repo")
            ref = m2.group("ref")
            if self.sha_regexp.match(ref):
                # SHA pin: the version it corresponds to is recorded in
                # the trailing comment, e.g. `@<sha> # v1.2.3`
                comment = m.group("comment")
                if not comment or not self.version_regexp.match(comment):
                    _log.debug("skip %s:%d: SHA pin without a version comment", filename, lineno)
                    continue
                current = comment
            else:
                current = ref
            _log.debug("checking %s/%s@%s", org, repo, current)
            newest = self.get_version_github_tag(f"{org}/{repo}")
            if newest and newest != current:
                _log.info("new version found: %s:%d %s/%s@%s -> %s",
                          filename, lineno, org, repo, current, newest)
                res.append({
                    "file": filename,
                    "line": lineno,
                    "endLine": lineno,
                    "title": "new version found",
                    "message": f"{current} -> {newest}",
                })
        _log.info("finish check %s", filename)
        return res


@cli.command()
@common_option
@click.argument("input", type=click.Path(dir_okay=False, file_okay=True, exists=True), nargs=-1)
def check_version(input):
    vc = VersionCheck()
    for i in input:
        _log.info("loading %s", click.format_filename(i))
        with open(i) as fp:
            text = fp.read()
        res = vc.check_version(i, text)
        if len(res) != 0:
            for l in res:
                click.echo("::notice file={file},line={line},endLine={endLine},title={title}::{message}".format(**l))


if __name__ == "__main__":
    cli()

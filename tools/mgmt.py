import click
import requests
import subprocess
import re
import functools
import yaml
from yaml.loader import SafeLoader
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
    action_regexp = re.compile(
        "^(?P<org>[a-z0-9A-Z_-]+)/(?P<repo>[a-z0-9A-Z_-]+)@(?P<version>v[0-9]+)$")
    version_regexp = re.compile("^(?P<version>v[0-9]+)$")

    def get_newest(self, val: list[str]) -> str:
        _log.debug("choose newest: %s", val)
        vers = natsorted([x for x in val if self.version_regexp.match(x)])
        _log.debug("sorted: %s", vers)
        if len(vers) != 0:
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

    def check_version(self, filename, ymldata) -> list[dict]:
        name = ymldata.get("name")
        _log.debug("data = %s", ymldata)
        _log.info("start check %s", filename)
        runs = ymldata.get("runs", {})
        res = []
        if runs.get("using") == "composite":
            for s in runs.get("steps", []):
                uses = s.get("uses")
                if uses:
                    _log.debug("checking0 %s", uses)
                    m = self.action_regexp.match(uses)
                    if not m:
                        continue
                    org = m.group("org")
                    repo = m.group("repo")
                    version = m.group("version")
                    _log.debug("checking %s/%s@%s", org, repo, version)
                    newest = self.get_version_github_tag(f"{org}/{repo}")
                    if newest != version:
                        _log.info("new version found: %s:%s %s/%s@%s -> %s",
                                  filename, s.get("__line__"), org, repo, version, newest)
                        res.append({
                            "file": filename,
                            "line": s.get("__line__"),
                            "endLine": s.get("__line__"),
                            "title": "new version found",
                            "message": f"{version} -> {newest}",
                        })
        _log.info("finish check %s", name)
        return res


class SafeLineLoader(SafeLoader):
    def construct_mapping(self, node, deep=False):
        mapping = super(SafeLineLoader, self).construct_mapping(
            node, deep=deep)
        # Add 1 so line numbering starts at 1
        mapping['__line__'] = node.start_mark.line + 1
        return mapping


@cli.command()
@common_option
@click.argument("input", type=click.Path(dir_okay=False, file_okay=True, exists=True), nargs=-1)
def check_version(input):
    vc = VersionCheck()
    for i in input:
        _log.info("loading %s", click.format_filename(i))
        with open(i) as fp:
            data = yaml.load(fp, Loader=SafeLineLoader)
        res = vc.check_version(i, data)
        if len(res) != 0:
            for l in res:
                click.echo("::notice file={file},line={line},endLine={endLine},title={title}::{message}".format(**l))


if __name__ == "__main__":
    cli()

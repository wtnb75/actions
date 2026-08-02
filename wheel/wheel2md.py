import argparse
import contextlib
import re
import sys

from pkginfo import Wheel


def escape_markdown(s: str) -> str:
    return re.sub(r"([_*~`])", r"\\\1", s)


@contextlib.contextmanager
def open_output(args):
    if args.output:
        with open(args.output, "w") as f:
            yield f
    elif args.append:
        with open(args.append, "a+") as f:
            yield f
    else:
        yield sys.stdout


def main():
    parser = argparse.ArgumentParser(
        prog="wheel2md",
        description="wheel to markdown",
    )
    parser.add_argument("filename")
    parser.add_argument("-o", "--output", action="store")
    parser.add_argument("-a", "--append", action="store")
    args = parser.parse_args()
    pkg = Wheel(args.filename)
    with open_output(args) as ofp:
        print(
            f"""
## package {pkg.name}

|      | description |
|------|-------------|
| metadata-version | {pkg.metadata_version} |
| Name | {pkg.name} |
| Version | {pkg.version} |
| Summary | {escape_markdown(pkg.summary)} |
| License | {pkg.license} |
| URL | {pkg.home_page} |
| Author | {pkg.author} <<{pkg.author_email}>> |
| Classifiers | {"<br/>".join(pkg.classifiers)} |
| Requires | {"<br />".join(pkg.requires_dist)} |
""",
            file=ofp,
        )


if __name__ == "__main__":
    main()

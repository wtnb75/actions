from pkginfo import Wheel
import argparse
import sys
import re


def escape_markdown(s: str) -> str:
    return re.sub(r'([_*~`])', r'\\\1', s)


def main():
    parser = argparse.ArgumentParser(
        prog="wheel2md",
        description="wheel to markdown",)
    parser.add_argument("filename")
    parser.add_argument("-o", "--output", action="store")
    parser.add_argument("-a", "--append", action="store")
    args = parser.parse_args()
    if args.output:
        ofp = open(args.output, "w")
    elif args.append:
        ofp = open(args.output, "a+")
    else:
        ofp = sys.stdout
    pkg = Wheel(args.filename)
    print(f"""
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
""", file=ofp)


if __name__ == "__main__":
    main()

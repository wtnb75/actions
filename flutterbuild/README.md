# flutter web build action

build flutter web release, embed coverage html report if present, ready
for actions/upload-pages-artifact


## example

```yaml
jobs:
  build:
    runs-on: ubuntu-latest
    steps:
    - uses: wtnb75/actions/flutter@main
    - id: flutterbuild
      uses: wtnb75/actions/flutterbuild@main
      with:
        base-href: value  # web base href (e.g. &#34;/reponame/&#34;) (REQUIRED)
        coverage-dir: value  # coverage html directory to embed at build/web/coverage (skipped if empty or missing)
```

# Inputs

| Name | Description | Default | Required |
|------|-------------|---------|----------|
| base-href | web base href (e.g. &#34;/reponame/&#34;) | n/a | True |
| coverage-dir | coverage html directory to embed at build/web/coverage (skipped if empty or missing) | coverage/html | False |

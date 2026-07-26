# python deps update action

update uv.lock and make PR


## example

```yaml
jobs:
  build:
    runs-on: ubuntu-latest
    steps:
    - uses: wtnb75/actions/python@main
    - id: pyupdate
      uses: wtnb75/actions/pyupdate@main
      with:
        github-token: value  # github token (REQUIRED)
        test-args: value  # if set, run `uv run pytest &lt;args&gt;` after update; PR is skipped when the test fails
        reviewers: value  # comma or newline separated GitHub usernames to request as PR reviewers
```

# Inputs

| Name | Description | Default | Required |
|------|-------------|---------|----------|
| github-token | github token | ${{ github.token }} | True |
| test-args | if set, run `uv run pytest &lt;args&gt;` after update; PR is skipped when the test fails | n/a | False |
| reviewers | comma or newline separated GitHub usernames to request as PR reviewers | ${{ github.repository_owner }} | False |

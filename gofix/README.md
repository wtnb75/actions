# go fix action

run `go fix` to rewrite deprecated API usage, then make PR


## example

```yaml
jobs:
  build:
    runs-on: ubuntu-latest
    steps:
    - uses: actions/setup-go@v5
    - id: gofix
      uses: wtnb75/actions/gofix@main
      with:
        github-token: value  # github token (REQUIRED)
        go-test-args: value  # if set, run `go test &lt;args&gt;` after fix; PR is skipped when the test fails
        reviewers: value  # comma or newline separated GitHub usernames to request as PR reviewers
        branch: value  # PR branch name
```

# Inputs

| Name | Description | Default | Required |
|------|-------------|---------|----------|
| github-token | github token | ${{ github.token }} | True |
| go-test-args | if set, run `go test &lt;args&gt;` after fix; PR is skipped when the test fails | n/a | False |
| reviewers | comma or newline separated GitHub usernames to request as PR reviewers | ${{ github.repository_owner }} | False |
| branch | PR branch name | chore/go-fix | False |

# gomod update action

update go.mod/go.sum and make PR


## example

```yaml
jobs:
  build:
    runs-on: ubuntu-latest
    steps:
    - uses: actions/setup-go@v5
    - id: goupdate
      uses: wtnb75/actions/goupdate@main
      with:
        github-token: value  # github token
        go-test-args: value  # if set, run `go test &lt;args&gt;` after update; PR is skipped when the test fails
        reviewers: value  # comma or newline separated GitHub usernames to request as PR reviewers
        branch: value  # PR branch name
```

# Inputs

| Name | Description | Default | Required |
|------|-------------|---------|----------|
| github-token | github token | ${{ github.token }} | False |
| go-test-args | if set, run `go test &lt;args&gt;` after update; PR is skipped when the test fails | n/a | False |
| reviewers | comma or newline separated GitHub usernames to request as PR reviewers | ${{ github.repository_owner }} | False |
| branch | PR branch name | chore/update-deps | False |

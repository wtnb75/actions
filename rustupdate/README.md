# rust deps update action

upgrade Cargo.toml dependency versions and make PR


## example

```yaml
jobs:
  build:
    runs-on: ubuntu-latest
    steps:
    - uses: wtnb75/actions/rust@main
    - id: rustupdate
      uses: wtnb75/actions/rustupdate@main
      with:
        github-token: value  # github token
        test-args: value  # if set, run `cargo test $TEST_ARGS` after update; PR is skipped when the test fails
        reviewers: value  # comma or newline separated GitHub usernames to request as PR reviewers
        branch: value  # PR branch name
```

# Inputs

| Name | Description | Default | Required |
|------|-------------|---------|----------|
| github-token | github token | ${{ github.token }} | False |
| test-args | if set, run `cargo test $TEST_ARGS` after update; PR is skipped when the test fails | n/a | False |
| reviewers | comma or newline separated GitHub usernames to request as PR reviewers | ${{ github.repository_owner }} | False |
| branch | PR branch name | chore/update-deps | False |

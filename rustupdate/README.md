# rust deps update action

upgrade Cargo.toml dependency versions and make PR


## example

```yaml
jobs:
  build:
    runs-on: ubuntu-latest
    steps:
    - uses: actions/setup-go@v5
    - uses: wtnb75/actions/rust@main
    - id: rustupdate
      uses: wtnb75/actions/rustupdate@main
      with:
        github-token: value  #  (REQUIRED)
        test-args: value  # if set, run `cargo test $TEST_ARGS` after update; PR is skipped when the test fails
        reviewers: value  # 
```

# Inputs

| Name | Description | Default | Required |
|------|-------------|---------|----------|
| github-token |  | ${{ github.token }} | True |
| test-args | if set, run `cargo test $TEST_ARGS` after update; PR is skipped when the test fails | n/a | False |
| reviewers |  | ${{ github.repository_owner }} | False |
# flutter deps update action

upgrade pubspec.yaml dependency versions and make PR


## example

```yaml
jobs:
  build:
    runs-on: ubuntu-latest
    steps:
    - uses: wtnb75/actions/flutter@main
    - id: flutterupdate
      uses: wtnb75/actions/flutterupdate@main
      with:
        github-token: value  # github token (REQUIRED)
        test-args: value  # if set, run `flutter test $TEST_ARGS` after update; PR is skipped when the test fails
        reviewers: value  # comma or newline separated GitHub usernames to request as PR reviewers
```

# Inputs

| Name | Description | Default | Required |
|------|-------------|---------|----------|
| github-token | github token | ${{ github.token }} | True |
| test-args | if set, run `flutter test $TEST_ARGS` after update; PR is skipped when the test fails | n/a | False |
| reviewers | comma or newline separated GitHub usernames to request as PR reviewers | ${{ github.repository_owner }} | False |

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
        github-token: value  #  (REQUIRED)
        test-args: value  # if set, run `flutter test $TEST_ARGS` after update; PR is skipped when the test fails
        reviewers: value  # 
```

# Inputs

| Name | Description | Default | Required |
|------|-------------|---------|----------|
| github-token |  | ${{ github.token }} | True |
| test-args | if set, run `flutter test $TEST_ARGS` after update; PR is skipped when the test fails | n/a | False |
| reviewers |  | ${{ github.repository_owner }} | False |

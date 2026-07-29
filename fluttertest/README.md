# flutter test + coverage action

run flutter test with coverage, emit lcov summary + html report


## example

```yaml
jobs:
  build:
    runs-on: ubuntu-latest
    steps:
    - uses: wtnb75/actions/flutter@main
    - id: fluttertest
      uses: wtnb75/actions/fluttertest@main
      with:
        html-output-dir: value  # coverage HTML report output directory
```

# Inputs

| Name | Description | Default | Required |
|------|-------------|---------|----------|
| html-output-dir | coverage HTML report output directory | coverage/html | False |

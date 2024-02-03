# pytest action

run pytest


## example

```yaml
jobs:
  build:
    runs-on: ubuntu-latest
    steps:
    - uses: actions/setup-python@v5
    - id: pytest
      uses: wtnb75/actions/pytest@main
      with:
        test-readme: value  # directory contains README.md to use pytest-readme
  use-artifact:
    needs: build
    runs-on: ubuntu-latest
    steps:
    - uses: actions/download-artifact@v4
      with:
        name: coverage
        path: path/to/artifact
    - name: show files in coverage
      run: ls -lR
      working-directory: path/to/artifact
      shell: bash
```

# Inputs

| Name | Description | Default | Required |
|------|-------------|---------|----------|
| test-readme | directory contains README.md to use pytest-readme | n/a | False |

# Artifacts

| Name | Description |
|------|-------------|
| coverage | coverage data |

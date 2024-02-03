# wheel action

build python package by calling setup.py bdist_wheel


## example

```yaml
jobs:
  build:
    runs-on: ubuntu-latest
    steps:
    - uses: actions/setup-python@v5
    - id: wheel
      uses: wtnb75/actions/wheel@main
      with:
        output-dir: value  # output directory (REQUIRED)
    - run: |
        echo "filename: ${{ steps.wheel.outputs.filename }}"
        echo "hash: ${{ steps.wheel.outputs.hash }}"
  use-artifact:
    needs: build
    runs-on: ubuntu-latest
    steps:
    - uses: actions/download-artifact@v4
      with:
        name: wheel
        path: path/to/artifact
    - name: show files in wheel
      run: ls -lR
      working-directory: path/to/artifact
      shell: bash
```

# Inputs

| Name | Description | Default | Required |
|------|-------------|---------|----------|
| output-dir | output directory | dist | True |

# Outputs

| Name | Description |
|------|-------------|
| filename | result file name |
| hash | result file hash |

# Artifacts

| Name | Description |
|------|-------------|
| wheel | wheel artifact |

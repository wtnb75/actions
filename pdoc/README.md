# pdoc action

run pdoc


## example

```yaml
jobs:
  build:
    runs-on: ubuntu-latest
    steps:
    - uses: actions/setup-python@v4
    - id: pdoc
      uses: wtnb75/actions/pdoc@main
      with:
        output-dir: value  # output directory (REQUIRED)
        module: value  # module to document (REQUIRED)
        other-options: value  # other option to pdoc
  use-artifact:
    needs: build
    runs-on: ubuntu-latest
    steps:
    - uses: actions/download-artifact@v3
      with:
        name: pdoc
        path: path/to/artifact
    - name: show files in pdoc
      run: ls -lR
      working-directory: path/to/artifact
      shell: bash
```

# Inputs

| Name | Description | Default | Required |
|------|-------------|---------|----------|
| output-dir | output directory | n/a | True |
| module | module to document | n/a | True |
| other-options | other option to pdoc | n/a | False |

# Artifacts

| Name | Description |
|------|-------------|
| pdoc | document data |

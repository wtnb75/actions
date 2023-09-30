# wheel action

build python package by calling setup.py bdist_wheel


## example

```yaml
- id: wheel
  uses: wtnb75/actions/wheel@main
  with:
    subcommand: value  # setup.py subcommand (REQUIRED)
    output-dir: value  # output directory (REQUIRED)
- run: |
    echo "filename: ${{ steps.wheel.outputs.filename }}"
```

# Inputs

| Name | Description | Default | Required |
|------|-------------|---------|----------|
| subcommand | setup.py subcommand | bdist_wheel | True |
| output-dir | output directory | dist | True |

# Outputs

| Name | Description |
|------|-------------|
| filename | result file name |

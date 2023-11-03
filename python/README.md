# python + pip install action

install python and pip install


## example

```yaml
jobs:
  build:
    runs-on: ubuntu-latest
    steps:
    - id: python
      uses: wtnb75/actions/python@main
      with:
        pipinstall: value  # pip install argument
    - run: |
        echo "python-version: ${{ steps.python.outputs.python-version }}"
        echo "python-path: ${{ steps.python.outputs.python-path }}"
        echo "cache-hit: ${{ steps.python.outputs.cache-hit }}"
```

# Inputs

| Name | Description | Default | Required |
|------|-------------|---------|----------|
| pipinstall | pip install argument | n/a | False |

# Outputs

| Name | Description |
|------|-------------|
| python-version | python version string |
| python-path | python executable path |
| cache-hit | cache hit or not |

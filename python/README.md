# python + uv sync action

install python and uv, then run `uv sync`


## example

```yaml
jobs:
  build:
    runs-on: ubuntu-latest
    steps:
    - id: python
      uses: wtnb75/actions/python@main
      with:
        python-version: value  # python version
        extra-args: value  # extra arguments for `uv sync` (e.g. &#34;--extra ssh&#34;)
    - run: |
        echo "python-version: ${{ steps.python.outputs.python-version }}"
        echo "python-path: ${{ steps.python.outputs.python-path }}"
        echo "cache-hit: ${{ steps.python.outputs.cache-hit }}"
```

# Inputs

| Name | Description | Default | Required |
|------|-------------|---------|----------|
| python-version | python version | 3.x | False |
| extra-args | extra arguments for `uv sync` (e.g. &#34;--extra ssh&#34;) | n/a | False |

# Outputs

| Name | Description |
|------|-------------|
| python-version | python version string |
| python-path | python executable path |
| cache-hit | cache hit or not |

# merge pages action

copy multiple directories for gh-pages


## example

```yaml
jobs:
  build:
    runs-on: ubuntu-latest
    steps:
    - uses: actions/setup-python@v5
    - id: merge-pages
      uses: wtnb75/actions/merge-pages@main
      with:
        output: value  # output directory (REQUIRED)
        dirs: value  # directories
        pydist: value  # python package directory
  deploy:
    needs: build
    runs-on: ubuntu-latest
    permissions:
      id-token: write
      pages: write
    environment:
      name: github-pages
      url: ${{ steps.deployment.outputs.page_url }}
    steps:
    - id: deployment
      uses: actions/deploy-pages@v4
```

# Inputs

| Name | Description | Default | Required |
|------|-------------|---------|----------|
| output | output directory | publish | True |
| dirs | directories | n/a | False |
| pydist | python package directory | n/a | False |

# Artifacts

| Name | Description |
|------|-------------|
| github-pages | merged pages |

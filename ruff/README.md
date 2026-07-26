# ruff linter action

lint by ruff


## example

```yaml
jobs:
  build:
    runs-on: ubuntu-latest
    steps:
    - id: ruff
      uses: wtnb75/actions/ruff@main
      with:
        dirs: value  # directories (REQUIRED)
```

# Inputs

| Name | Description | Default | Required |
|------|-------------|---------|----------|
| dirs | directories | . | True |

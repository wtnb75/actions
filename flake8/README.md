# flake8 linter action

lint by flake8


## example

```yaml
- id: flake8
  uses: wtnb75/actions/flake8@main
  with:
    flakeext: value  # flake8 extensions
    dirs: value  # directories (REQUIRED)
    flakeopts: value  # flake8 options
```

# Inputs

| Name | Description | Default | Required |
|------|-------------|---------|----------|
| flakeext | flake8 extensions | n/a | False |
| dirs | directories | n/a | True |
| flakeopts | flake8 options | --max-line-length=120 | False |

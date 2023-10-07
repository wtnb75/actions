# pytest action

run pytest


## example

```yaml
- id: pytest
  uses: wtnb75/actions/pytest@main
  with:
    test-readme: value  # directory contains README.md to use pytest-readme
```

# Inputs

| Name | Description | Default | Required |
|------|-------------|---------|----------|
| test-readme | directory contains README.md to use pytest-readme | n/a | False |

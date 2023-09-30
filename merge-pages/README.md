# merge-pages action

## example

```yaml
- id: merge-pages
  uses: wtnb75/actions/merge-pages@main
  with:
    output: value  # output directory (REQUIRED)
    dirs: value  # directories
    pydist: value  # python package directory
```

# Inputs

| Name | Description | Default | Required |
|------|-------------|---------|----------|
| output | output directory | publish | True |
| dirs | directories | n/a | False |
| pydist | python package directory | n/a | False |

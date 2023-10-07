# pdoc action

run pdoc


## example

```yaml
- id: pdoc
  uses: wtnb75/actions/pdoc@main
  with:
    output-dir: value  # output directory (REQUIRED)
    module: value  # module to document (REQUIRED)
    other-options: value  # other option to pdoc
```

# Inputs

| Name | Description | Default | Required |
|------|-------------|---------|----------|
| output-dir | output directory | n/a | True |
| module | module to document | n/a | True |
| other-options | other option to pdoc | n/a | False |

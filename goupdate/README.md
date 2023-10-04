# gomod update action

update go.mod/go.sum and make PR


## example

```yaml
- id: goupdate
  uses: wtnb75/actions/goupdate@main
  with:
    ghtoken: value  # github token (REQUIRED)
```

# Inputs

| Name | Description | Default | Required |
|------|-------------|---------|----------|
| ghtoken | github token | n/a | True |

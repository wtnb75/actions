# gomod update action

update go.mod/go.sum and make PR


## example

```yaml
- id: goupdate
  uses: wtnb75/actions/goupdate@main
  with:
    github-token: value  # github token (REQUIRED)
```

# Inputs

| Name | Description | Default | Required |
|------|-------------|---------|----------|
| github-token | github token | ${{ github.token }} | True |

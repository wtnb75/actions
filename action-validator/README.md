# actions-validator action

validate github actions yaml file


## example

```yaml
- id: action-validator
  uses: wtnb75/actions/action-validator@main
  with:
    files: value  # target yaml files (REQUIRED)
    version: value  # actions-validator version (REQUIRED)
```

# Inputs

| Name | Description | Default | Required |
|------|-------------|---------|----------|
| files | target yaml files | .github/workflows/*.y*ml | True |
| version | actions-validator version | v0.5.3 | True |

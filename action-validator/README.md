# actions-validator action

validate github actions yaml file


## example

```yaml
jobs:
  build:
    runs-on: ubuntu-latest
    steps:
    - id: action-validator
      uses: wtnb75/actions/action-validator@main
      with:
        files: value  # target yaml files
        repo: value  # actions-validator repository
        version: value  # actions-validator version
        sha256: value  # expected sha256 checksum of the action-validator_linux_amd64 binary for the pinned version
```

# Inputs

| Name | Description | Default | Required |
|------|-------------|---------|----------|
| files | target yaml files | .github/workflows/*.y*ml | False |
| repo | actions-validator repository | https://github.com/mpalmer/action-validator | False |
| version | actions-validator version | v0.5.3 | False |
| sha256 | expected sha256 checksum of the action-validator_linux_amd64 binary for the pinned version | deaa5dc8c6d3f3498c83b0d01c610ac430034d803746af056bd3b0041ad14781 | False |

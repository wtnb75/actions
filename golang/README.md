# golang setup + fmt/vet/lint action

setup go, then run gofmt/go vet/golangci-lint


## example

```yaml
jobs:
  build:
    runs-on: ubuntu-latest
    steps:
    - id: golang
      uses: wtnb75/actions/golang@main
      with:
        go-version: value  # go version
```

# Inputs

| Name | Description | Default | Required |
|------|-------------|---------|----------|
| go-version | go version | stable | False |

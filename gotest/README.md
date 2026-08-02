# go test + coverage action

run go test with coverage, optionally with extra build tags


## example

```yaml
jobs:
  build:
    runs-on: ubuntu-latest
    steps:
    - uses: actions/setup-go@v5
    - id: gotest
      uses: wtnb75/actions/gotest@main
      with:
        tags: value  # space-separated build tags to test additionally (e.g. &#39;wasmer wasmtime docker wazero&#39;)
        html-output-dir: value  # coverage HTML report output directory
```

# Inputs

| Name | Description | Default | Required |
|------|-------------|---------|----------|
| tags | space-separated build tags to test additionally (e.g. &#39;wasmer wasmtime docker wazero&#39;) | n/a | False |
| html-output-dir | coverage HTML report output directory | coverage | False |

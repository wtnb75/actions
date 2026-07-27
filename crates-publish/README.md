# crates.io publish action

publish crate to crates.io

## example

```yaml
jobs:
  build:
    runs-on: ubuntu-latest
    steps:
    - uses: actions/setup-go@v5
    - uses: wtnb75/actions/rust@main
    - id: crates-publish
      uses: wtnb75/actions/crates-publish@main
      with:
        token: value  # cargo registry token (CARGO_REGISTRY_TOKEN) (REQUIRED)
```

# Inputs

| Name | Description | Default | Required |
|------|-------------|---------|----------|
| token | cargo registry token (CARGO_REGISTRY_TOKEN) | n/a | True |
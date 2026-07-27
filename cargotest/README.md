# cargo test + coverage action

run cargo test with coverage via cargo-llvm-cov


## example

```yaml
jobs:
  build:
    runs-on: ubuntu-latest
    steps:
    - uses: wtnb75/actions/rust@main
    - id: cargotest
      uses: wtnb75/actions/cargotest@main
      with:
        html-output-dir: value  # coverage HTML report output directory
```

# Inputs

| Name | Description | Default | Required |
|------|-------------|---------|----------|
| html-output-dir | coverage HTML report output directory | coverage | False |

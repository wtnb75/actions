# rust setup + fmt/clippy action

setup rust stable toolchain, then run cargo fmt --check / cargo clippy


## example

```yaml
jobs:
  build:
    runs-on: ubuntu-latest
    steps:
    - uses: actions/setup-go@v5
    - id: rust
      uses: wtnb75/actions/rust@main
```
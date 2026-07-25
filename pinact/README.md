# pinact action

pin github actions references to SHA (and update existing pins to latest)


## example

```yaml
jobs:
  build:
    runs-on: ubuntu-latest
    steps:
    - uses: actions/setup-go@v5
    - id: pinact
      uses: wtnb75/actions/pinact@main
```

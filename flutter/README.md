# flutter setup + analyze action

setup flutter (web-only), regenerate gitignored platform boilerplate via
`flutter create .`, then run `flutter analyze`


## example

```yaml
jobs:
  build:
    runs-on: ubuntu-latest
    steps:
    - id: flutter
      uses: wtnb75/actions/flutter@main
      with:
        channel: value  # flutter channel
```

# Inputs

| Name | Description | Default | Required |
|------|-------------|---------|----------|
| channel | flutter channel | stable | False |

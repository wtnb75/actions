# node/pnpm setup action

install pnpm and node, then run `pnpm install --frozen-lockfile`


## example

```yaml
jobs:
  build:
    runs-on: ubuntu-latest
    steps:
    - id: node
      uses: wtnb75/actions/node@main
      with:
        working-directory: value  # directory containing package.json
        node-version: value  # node version
```

# Inputs

| Name | Description | Default | Required |
|------|-------------|---------|----------|
| working-directory | directory containing package.json | . | False |
| node-version | node version | lts/* | False |

# eslint action

lint by eslint (via `pnpm run lint`)


## example

```yaml
jobs:
  build:
    runs-on: ubuntu-latest
    steps:
    - uses: wtnb75/actions/node@main
    - id: eslint
      uses: wtnb75/actions/eslint@main
      with:
        working-directory: value  # directory containing package.json
```

# Inputs

| Name | Description | Default | Required |
|------|-------------|---------|----------|
| working-directory | directory containing package.json | . | False |

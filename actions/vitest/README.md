# vitest action

test by vitest (via `pnpm run test` / `pnpm run test:coverage`); does nothing
(and does not fail) if the repository has no matching script


## example

```yaml
jobs:
  build:
    runs-on: ubuntu-latest
    steps:
    - uses: wtnb75/actions/node@main
    - id: vitest
      uses: wtnb75/actions/vitest@main
      with:
        working-directory: value  # directory containing package.json
        coverage: value  # if true, run `test:coverage` instead of `test`
```

# Inputs

| Name | Description | Default | Required |
|------|-------------|---------|----------|
| working-directory | directory containing package.json | . | False |
| coverage | if true, run `test:coverage` instead of `test` | false | False |

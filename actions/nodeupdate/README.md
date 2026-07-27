# node deps update action

update pnpm-lock.yaml and make PR


## example

```yaml
jobs:
  build:
    runs-on: ubuntu-latest
    steps:
    - uses: wtnb75/actions/node@main
    - id: nodeupdate
      uses: wtnb75/actions/nodeupdate@main
      with:
        github-token: value  # github token (REQUIRED)
        working-directory: value  # directory containing package.json
        test-args: value  # if set, run `pnpm run &lt;args&gt;` after update; PR is skipped when it fails. omit this entirely for repos with no matching script
        reviewers: value  # comma or newline separated GitHub usernames to request as PR reviewers
```

# Inputs

| Name | Description | Default | Required |
|------|-------------|---------|----------|
| github-token | github token | ${{ github.token }} | True |
| working-directory | directory containing package.json | . | False |
| test-args | if set, run `pnpm run &lt;args&gt;` after update; PR is skipped when it fails. omit this entirely for repos with no matching script | n/a | False |
| reviewers | comma or newline separated GitHub usernames to request as PR reviewers | ${{ github.repository_owner }} | False |

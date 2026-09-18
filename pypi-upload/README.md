# pypi upload action

upload file to pypi

## example

```yaml
jobs:
  build:
    runs-on: ubuntu-latest
    steps:
    - uses: wtnb75/actions/python@main
    - id: pypi-upload
      uses: wtnb75/actions/pypi-upload@main
      with:
        username: value  # pypi username (use `__token__` when authenticating with an API token)
        password: value  # pypi password (or API token value when username is `__token__`) (REQUIRED)
        repository_url: value  # pypi url
        file: value  # upload file (REQUIRED)
```

# Inputs

| Name | Description | Default | Required |
|------|-------------|---------|----------|
| username | pypi username (use `__token__` when authenticating with an API token) | __token__ | False |
| password | pypi password (or API token value when username is `__token__`) | n/a | True |
| repository_url | pypi url | https://upload.pypi.org/legacy/ | False |
| file | upload file | n/a | True |

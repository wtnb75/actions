# pypi upload action

upload file to pypi

## example

```yaml
- id: pypi-upload
  uses: wtnb75/actions/pypi-upload@main
  with:
    username: value  # pypi userrname (REQUIRED)
    password: value  # pypi password (REQUIRED)
    repository_url: value  # pypi url
    file: value  # upload file (REQUIRED)
```

# Inputs

| Name | Description | Default | Required |
|------|-------------|---------|----------|
| username | pypi userrname | ${{ github.actor }} | True |
| password | pypi password | n/a | True |
| repository_url | pypi url | https://upload.pypi.org/legacy/ | False |
| file | upload file | n/a | True |

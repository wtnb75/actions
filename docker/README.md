# docker action

build docker image and push to registry


## example

```yaml
jobs:
  build:
    runs-on: ubuntu-latest
    steps:
    - id: docker
      uses: wtnb75/actions/docker@main
      with:
        username: value  # docker username (REQUIRED)
        password: value  # docker password (REQUIRED)
        registry: value  # registry hostname
        image-name: value  # image name (REQUIRED)
        image-version: value  # set label
        context: value  # context directory (REQUIRED)
        build-args: value  # build args
        platforms: value  # image platforms
        push: value  # push
    - run: |
        echo "imageid: ${{ steps.docker.outputs.imageid }}"
        echo "digest: ${{ steps.docker.outputs.digest }}"
        echo "metadata: ${{ steps.docker.outputs.metadata }}"
        echo "image-name: ${{ steps.docker.outputs.image-name }}"
```

# Inputs

| Name | Description | Default | Required |
|------|-------------|---------|----------|
| username | docker username | ${{ github.actor }} | True |
| password | docker password | n/a | True |
| registry | registry hostname | ghcr.io | False |
| image-name | image name | ${{ github.repository }} | True |
| image-version | set label | n/a | False |
| context | context directory | n/a | True |
| build-args | build args | n/a | False |
| platforms | image platforms | linux/amd64,linux/arm64 | False |
| push | push | false | False |

# Outputs

| Name | Description |
|------|-------------|
| imageid | image id |
| digest | image digest |
| metadata | build metadata |
| image-name | image name to pull |

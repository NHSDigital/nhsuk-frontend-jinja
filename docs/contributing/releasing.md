# Releasing

1. Create and push a new tag for the new version:

    ```sh
    git tag -a x.y.z
    git push x.y.z
    ```

2. Verify that the Github actions workflow has released the package to [PyPI](https://pypi.org/project/nhsuk-frontend-jinja/).
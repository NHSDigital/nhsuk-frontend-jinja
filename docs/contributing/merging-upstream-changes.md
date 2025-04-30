## Merging upstream changes

1. Run `npm update nhsuk-frontend`
2. in `pyproject.toml` update the version: if a major update of nhsuk-frontend, update the major version, otherwise, update the minor version.
3. update the [compataibility section of the readme](../README.md#Compatibility).
4. Check which components have changed in the last update, and make the corresponding changes in this package.
5. Run `npm run lint` to check for Nunjucks/Jinja incompatibilities, and review the [coding standards](./coding-standards.md) for other differences between Jinja and Nunjucks.
6. [Run the app locally](./running-locally.md) to manually check the components.
7. Run `npm run test:visual` to visually see what's changed.
8. Run `npm run test` (TODO) to check the templates generate the same HTML as `nhsuk-frontend`.
9. Run `npm run test:visual:approve` to approve any visual changes.
10. Create a pull request with the changes.

Next: [Releasing](releasing.md)

## Merging upstream changes

1. Run `npm install nhsuk-frontend@latest`
2. in `pyproject.toml` update the version: if a major update of nhsuk-frontend, update the major version, otherwise, update the minor version.
3. update the [compataibility section of the readme](../README.md#Compatibility).
4. Check which components have changed in the last update using the ([compare view](https://github.com/nhsuk/nhsuk-frontend/compare/v9.3.0...v9.5.2)) and [changelog](https://github.com/nhsuk/nhsuk-frontend/blob/main/CHANGELOG.md). Files to check:
   - *.njk files in `app/`
   - *.njk files in `packages/components/`
   - backstop.config.js
5. Update the `app/` directory with any changes to the examples
6. Update the `nhsuk_frontend_jinja/components` with any changes to the components themselves
7. Run `npm run lint` to check for Nunjucks/Jinja incompatibilities, and review the [coding standards](./coding-standards.md) for other differences between Jinja and Nunjucks.
8. [Run the app locally](./running-locally.md) to manually check the components.
9. Run `npm run test:visual` to visually see what's changed.
10. Run `npm run test` (TODO) to check the templates generate the same HTML as `nhsuk-frontend`.
11. Run `npm run test:visual:approve` to approve any visual changes.
12. Update the changelog
13. Create a pull request with the changes.

Next: [Releasing](releasing.md)

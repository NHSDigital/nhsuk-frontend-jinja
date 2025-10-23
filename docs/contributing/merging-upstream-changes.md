## Merging upstream changes

1. Run `npm install nhsuk-frontend@latest`
2. in `pyproject.toml` update the version: if a major update of nhsuk-frontend, update the major version, otherwise, update the minor version.
3. update the [compatibility section of the readme](../../README.md#Compatibility).
4. Check which components, macros and templates have changed in the last update using the ([compare view](https://github.com/nhsuk/nhsuk-frontend/compare/v10.0.0...v10.1.0)) and [changelog](https://github.com/nhsuk/nhsuk-frontend/blob/main/CHANGELOG.md). Files to check:
   - `template.njk` files in `packages/nhsuk-frontend/src/nhsuk`
   - `*.njk` files in `packages/nhsuk-frontend/src/nhsuk/components`
   - `*.njk` files in `packages/nhsuk-frontend/src/nhsuk/macros`
5. Update corresponding `*.jinja` files in `nhsuk_frontend_jinja/templates/nhsuk` with any changes
6. If necessary, make sure to add `*.jinja` files for any new components, macros and templates
7. Run `poetry run djlint -` to check for Nunjucks/Jinja incompatibilities, and review the [coding standards](./coding-standards.md) for other differences between Jinja and Nunjucks.
9. Run `poetry run pytest` to check the templates generate the same HTML as `nhsuk-frontend`.
10. Update the changelog
11. Create a pull request with the changes.

Next: [Releasing](releasing.md)

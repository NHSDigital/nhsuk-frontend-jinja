# Application architecture

The application generates static HTML pages to preview components, with each component having their own page, these files can be found in `app/`. To make changes to components, you will have to edit the individual components files within `templates/`. These are usually the only 2 folders that you will need.

---

`.github/`

GitHub specific files, such templates for pull requests and issues.

`app/`

Jinja (HTML) files for the component example pages that you see at http://localhost:3000/nhsuk-frontend when running the application locally and on https://nhsuk.github.io/nhsuk-frontend

`dist/` (Automatically generated)

Automatically generated compiled files and build assets for GitHub pages, releases and python packages. Don't manually edit files in this folder as they will be deleted.

`docs/`

Markdown files for documentation on GitHub, such as contributing to the project, coding standards and more.

`node_modules/` (Automatically generated)

Node package manager modules for third party dependencies. This folder is automatically generated when running `npm install`. Don't manually edit files in this folder as they will be deleted.

`nhsuk_frontend_jinja/templates/`

The Jinja HTML templates.

`tests/`

Test configuration files for our visual regression testing framework BackstopJS.
TODO: add tests to verify identical output with upstream.

---

Next: [Coding standards and style guide](coding-standards.md)

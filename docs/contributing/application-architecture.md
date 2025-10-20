# Application architecture

The application follows instructions to [test if your HTML matches NHS.UK frontend](https://github.com/nhsuk/nhsuk-frontend/blob/main/docs/contributing/testing-your-html.md). To make changes to components, you will have to edit the individual components files within `templates/`.

---

`.github/`

GitHub specific files, such templates for pull requests and issues.

`docs/`

Markdown files for documentation on GitHub, such as contributing to the project, coding standards and more.

`node_modules/` (Automatically generated)

Node package manager modules for third party dependencies. This folder is automatically generated when running `npm install`. Don't manually edit files in this folder as they will be deleted.

`nhsuk_frontend_jinja/templates/`

The Jinja HTML templates.

`tests/`

Unit tests for testing compatibility with `nhsuk-fronted`.

---

Next: [Coding standards and style guide](coding-standards.md)

# NHS.UK frontend jinja changelog

## Unreleased

## 0.4.0 - 14 July 2025

- Update to [nhsuk-frontend v1.0.0]()

### Breaking changes

Rename details component `text` param to `summaryText`:

```
  {{ details({
-   "text": "Where can I find my NHS number?",
+   "summaryText": "Where can I find my NHS number?",
    "html": "<p>An NHS number is a 10 digit number, like 485 777 3456.</p>"
  }) }}
```

### Fixes

nhsuk-frontend-jinja templates are now tested to be HTML equivalent to the Nunjucks versions in nhsuk-frontend.

This fixes `aria-describedby` not being added correctly in previous versions.

## 0.3.1 - 5 June 2025

- Update to [nhsuk-frontend v9.6.2](https://github.com/nhsuk/nhsuk-frontend/blob/main/CHANGELOG.md#962---9-june-2025).

## 0.3.0 - 5 June 2025

- Update to [nhsuk-frontend v9.6.1](https://github.com/nhsuk/nhsuk-frontend/blob/main/CHANGELOG.md#961---22-may-2025).

## 0.2.0 - 15 May 2025

- Update to [nhsuk-frontend v9.5.2](https://github.com/nhsuk/nhsuk-frontend/blob/main/CHANGELOG.md#952---14-may-2025).
- Document use of the page template.

## 0.1.0 (Prerelease) - 15 April 2025

:tada: **Initial release of the NHS.UK frontend Jinja templates**

- Initial release, including all templates from nhsuk-frontend v9.3.0.

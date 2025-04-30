# NHS.UK frontend jinja templates

A Jinja implementation of the [NHS.UK frontend](https://github.com/nhsuk/nhsuk-frontend) components.

NHS.UK frontend contains the code you need to start building user interfaces for NHS websites and services.

## Installation

We have not yet set up publishing to the Python Package Index (PyPI). In the meantime, you can install directly from GitHub:

```sh
pip install nhsuk-frontend-jinja
```

### Compatibility

The following table shows the version of NHS.UK frontend jinja that you should use for your targeted version of NHS.UK frontend:

| NHS.UK frontend version | NHS.UK frontend jinja version |
| -- | -- |
| 9.3.0 | 0.1.0 |

## Usage

Visit the [NHS digital service manual](https://service-manual.nhs.uk/) for examples of components and guidance for when to use them.

These templates require you to configure your Jinja environment to use `ChainableUndefined` and the package loader.

Flask example:

```python
from jinja2 import FileSystemLoader, PackageLoader, ChainableUndefined

app.jinja_options = {
    "undefined": ChainableUndefined,  # This is needed to prevent jinja from throwing an error when chained parameters are undefined
    "loader": ChoiceLoader(
        [
            FileSystemLoader(PATH_TO_YOUR_TEMPLATES),
            PackageLoader("nhsuk_frontend_jinja"),
        ]
    ),
}
```

Plain Jinja example

```python
from jinja2 import FileSystemLoader, PackageLoader, ChainableUndefined

jinja_env = Environment(
    undefined=ChainableUndefined,
    loader=ChoiceLoader(
        FileSystemLoader(PATH_TO_YOUR_TEMPLATES),
        PackageLoader("nhsuk_frontend_jinja"),
    ),
    **options)
```

All our macros take identical arguments to the Nunjucks ones, except you need to quote the parameter names.

```jinja
{% from 'components/warning-callout/macro.jinja' import warningCallout %}

{{ warningCallout({
  "heading": "Quotey McQuoteface",
  "HTML": "<p>Don't forget to quote your parameter names!</p>"
}) }}
```

Note that all macro paths must be prefixed with `components/` and have the `.jinja` extension.

## Contribute

Read our [contributing guidelines](CONTRIBUTING.md) to contribute to NHS.UK frontend jinja.

## Development environment

[![Gitpod ready-to-code](https://img.shields.io/badge/Gitpod-ready--to--code-blue?logo=gitpod)](https://gitpod.io/#https://github.com/NHSDigital/nhsuk-frontend-jinja)

## Get in touch

This repo is maintained by NHS England.
Open a [GitHub issue](https://github.com/NHSDigital/nhsuk-frontend-digital/issues/new) if you need to get in touch.

## Licence

The codebase is released under the MIT Licence, unless stated otherwise. This covers both the codebase and any sample code in the documentation. The documentation is © NHS England and available under the terms of the Open Government 3.0 licence.

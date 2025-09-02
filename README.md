# NHS.UK frontend jinja templates

[![Quality Gate Status](https://sonarcloud.io/api/project_badges/measure?project=NHSDigital_nhsuk-frontend-jinja&metric=alert_status)](https://sonarcloud.io/summary/new_code?id=NHSDigital_nhsuk-frontend-jinja)

A Jinja implementation of the [NHS.UK frontend](https://github.com/nhsuk/nhsuk-frontend) components.

NHS.UK frontend contains the code you need to start building user interfaces for NHS websites and services.

## Installation

```sh
pip install nhsuk-frontend-jinja
```

### Compatibility

The following table shows the version of NHS.UK frontend jinja that you should use for your targeted version of NHS.UK frontend:

| NHS.UK frontend version | NHS.UK frontend jinja version |
| -- | -- |
| 9.3.0 | 0.1.0 |
| 9.5.2 | 0.2.0 |
| 9.6.1 | 0.3.0 |
| 9.6.2 | 0.3.1 |
| 10.0.0 | 0.4.1 |

### Configuration

Configure your Jinja environment to load templates from this package and use `ChainableUndefined`.

Flask example:

```python
from jinja2 import FileSystemLoader, ChoiceLoader, PackageLoader, ChainableUndefined

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

Plain Jinja example:

```python
from jinja2 import Environment, FileSystemLoader, ChoiceLoader, PackageLoader, ChainableUndefined

jinja_env = Environment(
    undefined=ChainableUndefined,
    loader=ChoiceLoader([
        FileSystemLoader(PATH_TO_YOUR_TEMPLATES),
        PackageLoader("nhsuk_frontend_jinja"),
    ]),
    **options)
```

Alternatively, if you want to reference components without the 'nhsuk/components' or 'nhsuk/macros' prefixes, you can include additional `PackageLoaders` that specify `package_path`:

```python
ChoiceLoader([
    FileSystemLoader(PATH_TO_YOUR_TEMPLATES),

    PackageLoader("nhsuk_frontend_jinja", package_path="templates/nhsuk/components"),
    PackageLoader("nhsuk_frontend_jinja", package_path="templates/nhsuk/macros"),

    PackageLoader("nhsuk_frontend_jinja"),
])
```

You should then be able to extend the [default page template](https://service-manual.nhs.uk/design-system/styles/page-template):

```jinja
{% extends 'nhsuk/template.jinja' %}

{% block pageTitle %}Example - NHS.UK Frontend{% endblock %}

{% block content %}
{% endblock %}
```

See [Page Template](https://service-manual.nhs.uk/design-system/styles/page-template) in the service manual for details of all the options.

## Usage

Visit the [NHS digital service manual](https://service-manual.nhs.uk/design-system) for examples of components and guidance for when to use them.

All our macros take identical arguments to the Nunjucks ones, except you need to quote the parameter names.

```jinja
{% from 'nhsuk/warning-callout/macro.jinja' import warningCallout %}

{{ warningCallout({
  "heading": "Quotey McQuoteface",
  "HTML": "<p>Don't forget to quote your parameter names!</p>"
}) }}
```

Note that all macro paths use the `.jinja` extension.

## Contribute

Read our [contributing guidelines](CONTRIBUTING.md) to contribute to NHS.UK frontend jinja.

## Development environment

[![Gitpod ready-to-code](https://img.shields.io/badge/Gitpod-ready--to--code-blue?logo=gitpod)](https://gitpod.io/#https://github.com/NHSDigital/nhsuk-frontend-jinja)

## Get in touch

This repo is maintained by NHS England.
Open a [GitHub issue](https://github.com/NHSDigital/nhsuk-frontend-digital/issues/new) if you need to get in touch.

## Licence

The codebase is released under the MIT Licence, unless stated otherwise. This covers both the codebase and any sample code in the documentation. The documentation is © NHS England and available under the terms of the Open Government 3.0 licence.

# NHS.UK frontend jinja changelog

## Unreleased

- Supports [nhsuk-frontend v10.1.0](https://github.com/nhsuk/nhsuk-frontend/compare/v10.0.0...v10.1.0).
- This includes small checkboxes and radios, numbered pagination and localisation for every component.
- See the [nhsuk-frontend changelog](https://github.com/nhsuk/nhsuk-frontend/blob/main/CHANGELOG.md) for further details.

### :new: **New features**

#### Localise character count component

You can now translate the text used by the [character count](https://service-manual.nhs.uk/design-system/components/character-count) component to:

- show when the maximum number of characters or words is reached
- show the number of characters or words over or under the allowed maximum
- update the textarea description if JavaScript is not available
- announce to screen readers when the textarea is focused

The macro accepts new options so you can customise each message. You can:

- Use `charactersAtLimitText` or `wordsAtLimitText` to provide the text that shows when users have reached the limit.
- Use `charactersUnderLimitText` or `wordsUnderLimitText` to provide the text that shows when users are under the limit. The component will pluralise the message according to the configured locale and the number of characters or words remaining.
- Use `charactersOverLimitText` or `wordsOverLimitText` to provide the text that shows when users are over the limit. The component will pluralise the message according to the configured locale and the number of characters or words remaining.
- Use `textareaDescriptionText` to provide the textarea description for assistive technologies. It is visible on the page when JavaScript is unavailable.

The component will replace `%{count}` with the number of characters over or under the limit.

If you're not using macros, you can use data-\* attributes to provide these translations. Within the attribute value, any [quotation marks or other characters reserved by HTML](https://developer.mozilla.org/en-US/docs/Glossary/Character_reference) needs to be converted into their HTML entity equivalents.

You can:

- use `data-i18n.characters-at-limit` or `data-i18n.words-at-limit` for when users are at the limit
- configure the text that informs the end user they are under the character or word limit, by using `data-i18n.characters-under-limit.{other,many,few,two,one,zero}` or `data-i18n.words-under-limit.{other,many,few,two,one,zero}`, with one suffix for each plural form required by your locale
- configure the text that informs the end user they are over the character or word limit, by using `data-i18n.characters-over-limit.{other,many,few,two,one,zero}` or `data-i18n.words-over-limit.{other,many,few,two,one,zero}`, with one suffix for each plural form required by your locale
- configure the description provided to assistive technologies when users focus the input, by using `data-i18n.textarea-description.{other,many,few,two,one,zero}` to provide the text to set as the description

You can also provide these messages using a JavaScript configuration object when creating an instance of the component or initialising all components. See [our guidance on localising NHS.UK frontend](/docs/configuration/localisation.md) for how to do this.

#### Smaller versions of radio buttons and checkboxes

You can now use smaller versions of the [radios](https://service-manual.nhs.uk/design-system/components/radios) and [checkboxes](https://service-manual.nhs.uk/design-system/components/checkboxes) components by adding the `nhsuk-radios--small` or `nhsuk-checkboxes--small` class.

#### Updated macro options for components

For consistency with other components, we’ve added new macro options:

- Back link `visuallyHiddenText` option
- Breadcrumbs nested `backLink` component option
- Contents list `landmarkLabel` and `visuallyHiddenTitle` options
- Do and Don't list `prefixText` option, with nested item `text` and `html` options
- Fieldset `html` and `role` options
- Header navigation `toggleMenuText` and `toggleMenuVisuallyHiddenText` options
- Inset text `visuallyHiddenText` option
- Pagination `previous`, `next` and `landmarkLabel` options
- Radios item `disabled` and `attributes` options
- Text input `autocapitalize` and `disabled` options, with prefix and suffix nested `text`, `html`, `classes` and `attributes` options
- Textarea `disabled` and `spellcheck` options
- Warning callout `visuallyHiddenText` option

Visit the [design system in the NHS digital service manual](https://service-manual.nhs.uk/design-system/components) to see macro options for each component.

#### Insert custom HTML into component form group wrappers

You can now insert custom HTML into form group wrappers for all components with form fields.

```njk
{{ input({
  "formGroup": {
    "beforeInput": {
      "html": "example"
    },
    "afterInput": {
      "html": "example"
    }
  }
}) }}
```

#### Numbered pagination component

The pagination component now supports numbered pagination, for example where you have a long list of of items to navigate.

You can use it like this:

```njk
pagination({
  "previous": {
    "href": "#"
  },
  "next": {
    "href": "#"
  },
  "items": [
    {
      "number": 1,
      "href": "#"
    },
    {
      "number": 2,
      "href": "#",
      "current": true
    },
    {
      "number": 3,
      "href": "#"
    }
  ]
})
```

### :recycle: **Changes**

#### Do and Don't list macro options

For consistency with other components, the do and don't list macro options have changed. The previous names are deprecated and will be removed in a future release.

If you're using the `list` macro in your service, you should update the nested `items` option, using `text` or `html` instead of `item`.

```patch
  {{ list({
    "title": "Do",
    "type": "tick",
    "items": [
      {
-       "item": "cover blisters with a soft plaster or padded dressing"
+       "text": "cover blisters with a soft plaster or padded dressing"
      },
      {
-       "item": "wash your hands before touching a burst blister"
+       "text": "wash your hands before touching a burst blister"
      },
      {
-       "item": "allow the fluid in a burst blister to drain before covering it with a plaster or dressing"
+       "text": "allow the fluid in a burst blister to drain before covering it with a plaster or dressing"
      }
    ]
  }) }}
```

#### Pagination macro options

For consistency with other components, the pagination macro options have changed. The previous names are deprecated and will be removed in a future release.

If you're using the `pagination` macro in your service, you should:

- replace the `previousUrl` option with the nested `previous.href` option
- replace the `previousPage` option with the nested `previous.labelText` option
- replace the `nextUrl` option with the nested `next.href` option
- replace the `nextPage` option with the nested `next.labelText` option

```patch
  {{ pagination({
-   "previousPage": "Treatments",
-   "previousUrl": "/section/treatments",
+   "previous": {
+     "labelText": "Treatments",
+     "href": "/section/treatments"
+   },
-   "nextPage": "Symptoms",
-   "nextUrl": "/section/symptoms"
+   "next": {
+     "labelText": "Symptoms",
+     "href": "/section/symptoms"
+   }
  }) }}
```

## 0.4.1 - 2 September 2025

Reintroduced `templates/` into the templates path so as not to break Jinja conventions.

Any `PackageLoader` configuration making use of the `package_path` argument should now use:

```python
PackageLoader("nhsuk_frontend_jinja", package_path="templates/nhsuk/components"),
PackageLoader("nhsuk_frontend_jinja", package_path="templates/nhsuk/macros"),
```

## 0.4.0 - 2 September 2025

- Supports [nhsuk-frontend v10.0.0](https://github.com/nhsuk/nhsuk-frontend/compare/v9.6.4...v10.0.0).
- This includes redesigns of the header and footer components.
- See the [nhsuk-frontend changelog](https://github.com/nhsuk/nhsuk-frontend/blob/main/CHANGELOG.md) for further details.
- Renamed the template path (see breaking changes below)

### :boom: **Breaking changes**

#### Jinja2 environment configuration

The top level template path has changed from `templates` to `nhsuk`, to more closely match `nhsuk-frontend`, and to avoid confusion
if multiple design systems are used in the same application.

In your app configuration, change any `PackageLoader` that pass a `package_path`:

Before:

```python
PackageLoader("nhsuk_frontend_jinja", package_path="templates/components"),
PackageLoader("nhsuk_frontend_jinja", package_path="templates/macros"),
```

After:

```python
PackageLoader("nhsuk_frontend_jinja", package_path="nhsuk/components"),
PackageLoader("nhsuk_frontend_jinja", package_path="nhsuk/macros"),
```

Templates extending from the base template must now include the `nhsuk` prefix.

Before:

```jinja
{% extends "template.jinja" %}
```

After:

```jinja
{% extends "nhsuk/template.jinja" %}
```

Any imports starting with `templates/` should be changed to `nhsuk/` as well.

#### Details component

Rename details component `text` param to `summaryText`:

```
  {{ details({
-   "text": "Where can I find my NHS number?",
+   "summaryText": "Where can I find my NHS number?",
    "html": "<p>An NHS number is a 10 digit number, like 485 777 3456.</p>"
  }) }}
```

#### Header component

If you're using the `header` macro in your service, you must:

- Rename the `transactionalService` option to the new `service` option, and remove the boolean `transactional` option.
- Replace the `primaryLinks` option with the nested `navigation.items` option, using `text` and `href` instead of `label` and `url`.
- Replace the `searchAction` option with the nested `search.action` option.
- Replace the `searchInputName` option with the nested `search.name` option.
- Remove the boolean `showNav` and `showSearch` options. The respective parts of the header are now shown automatically when `navigation.items` or `search` options are provided.
- Check the `classes` option for `nhsuk-header--white-nav` and remove it. To turn the navigation white, add the modifier class `nhsuk-header__navigation--white` to the nested `navigation.classes` option.
- Remove the `nhsuk-header__navigation-list--left-aligned` modifier class, navigation items are now aligned left by default.

To restore the previous justified alignment, where navigation items appeared evenly spaced out, add the new `nhsuk-header__navigation--justified` modifier class to the nested `navigation.classes` option.

#### Footer component

If you're using the `footer` macro in your service, you must:

- Replace the `links` option with the nested `navigation.items` option.
- Replace the `metaLinks` option with the nested `meta.items` option.
- Update all items to rename `label` to `text` and `URL` to `href`.

Before:

```jinja
{% block footer %}
  {{ footer({
    "links": [
      {
        "label": "NHS sites",
        "URL": "https://www.nhs.uk/nhs-sites"
      },
      {
        "label": "About us",
        "URL": "https://www.nhs.uk/about-us"
      },
      {
        "label": "Give us feedback",
        "URL": "https://www.nhs.uk/give-feedback-about-the-nhs-website/"
      }
    ],
    "metaLinks": [
      {
        "label": "Accessibility",
        "URL": "https://www.nhs.uk/accessibility/"
      },
      {
        "label": "Our policies",
        "URL": "https://www.nhs.uk/our-policies/"
      }
    ]
  }) }}
{% endblock %}
```

After:

```jinja
{% block footer %}
  {{ footer({
    "navigation": {
      "items": [
        {
          "text": "NHS sites",
          "href": "https://www.nhs.uk/nhs-sites"
        },
        {
          "text": "About us",
          "href": "https://www.nhs.uk/about-us"
        },
        {
          "text": "Give us feedback",
          "href": "https://www.nhs.uk/give-feedback-about-the-nhs-website/"
        }
      ]
    },
    "meta": {
      "items": [
        {
          "href": "https://www.nhs.uk/accessibility/",
          "text": "Accessibility"
        },
        {
          "href": "https://www.nhs.uk/our-policies/",
          "text": "Our policies"
        }
      ]
    }
  }) }}
{% endblock %}
```

#### Error summary component

If you've linked from an [error summary](https://design-system.service.gov.uk/components/error-summary/) component to the first input in a [radios](https://design-system.service.gov.uk/components/radios/) or [checkboxes](https://design-system.service.gov.uk/components/checkboxes/) component, the link may no longer work.

This is because the `id` of the first checkbox or radio item no longer has the suffix `-1`.

If you're using the `errorSummary` macro, remove `-1` from the end of the `href` attribute:

```patch
  {{ errorSummary({
    "titleText": "There is a problem",
    "errorList": [
      {
        "text": "Select how you like to be contacted",
-       "href": "#contact-preference-1"
+       "href": "#contact-preference"
      }
    ]
  }) }}
```

#### Rename component `HTML` param to `html`

If you're using the `card`, `details`, `insetText` or `warningCallout` macros, you need to rename the `HTML` param to `html`:

```patch
  {{ insetText({
-   "HTML": "<p>You'll need to stay away from school, nursery or work until all the spots have crusted over. This is usually 5 days after the spots first appeared.</p>"
+   "html": "<p>You'll need to stay away from school, nursery or work until all the spots have crusted over. This is usually 5 days after the spots first appeared.</p>"
  }) }}
```

### :wrench: **Fixes**

- nhsuk-frontend-jinja now tests all examples from `nhsuk-frontend` to make sure the rendered HTML is the same.

- `aria-describedby` is no longer missing from the rendered HTML.

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

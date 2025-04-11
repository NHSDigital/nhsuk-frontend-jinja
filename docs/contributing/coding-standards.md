# Coding standards

- [Consistency with NHS.UK frontend](#consistency)
- [Jinja](#jinja)

---

## Consistency

Templates should be changed as little as possible from those in the upstream [NHS.UK frontend package](https://github.com/nhsuk/nhsuk-frontend/pull/1199).

The less differences there are, the easier it is to update and bring in new changes from upstream.

The HTML output should be identical to the output of the NHS.UK frontend package (including whitespace).

---

## Jinja
The NHS.UK frontend components use Nunjucks as their templating language. Nunjucks is based on [Jinja](https://jinja.palletsprojects.com/en/stable/) and we have restricted ourselves to a subset of Jinja so that our templates can be rendered by both template engines (currently only the radios component cannot be rendered by Nunjucks). Maintaining Nunjucks compatibility leaves open the option of merging our work into the official NHS.UK frontend package.

Components are packaged as reusable chunks of code: macros. Developers import macros into their application, call them as per documentation and provide data to its arguments.

To provide a level of consistency for developers we have standardised argument names, their expected input, use and placement.

### Specifying content

When providing _content_ to a macro, say for a label or a button, we accept two argument options:

- `text` accepts a plain string and is the default way of passing content
- `html` accepts html markup. In the template we will not escape html so it will be rendered. In a scenario where both text and html are set, html argument will take precedence over text.

Example:

```
{{ insetText({
  "text": "You'll need to stay away from school, nursery or work until all the spots have crusted over. This is usually 5 days after the spots first appeared."
}) }}
```

```
{{ insetText({
  "html": "<p>If you drive you must tell the <a href='https://www.gov.uk/contact-the-dvla/' title='External website'>DVLA</a> about your vertigo. Visit the GOV.UK website for more information on <a href='https://www.gov.uk/dizziness-and-driving' title='External website'>driving with vertigo</a></p>"
}) }}
```

Example of implementing logic in a component template:

`{{ params.html | safe if params.html else params.text }}`

Example shows that if `html` and `text` arguments are present, then `html` takes precedence over `text` and we are not escaping it.

### Naming attributes

We should use **camelCase** for naming attributes.

### Specifying multiple items

When a component accepts a _single array of items_ for an output, such as checkboxes or radios, we accept an **_"items"_** array of objects. Table component is an exception is it can contain multiple array for rows, head, footer where there is need to for more specific names.

However, when accessing an items param, use square bracket syntax instead of dotted syntax:

Bad (clashes with `dict.items()` in Jinja):

```
{% for item in params.items %}
```

Good:

```
{% set items = params['items'] if 'items' in params else [] %}

{% for item in items %}
```

### Use of classes to specify variants

When a component has multiple visual presentations, such as the care cards, we make use of classes argument to differentiate between them.

Care card urgent (red) example:

```html
<div class="nhsuk-card nhsuk-card--care nhsuk-card--care--urgent">
```

Care card emergency (red and black) example:

```html
<div class="nhsuk-card nhsuk-card--care nhsuk-card--care--emergency">
```

### Use `~` for string concatenation

Prefer the `~` operator over the `+` operator. This will coerce all operands to strings without relying on Nunjucks-specific behaviour.

### Quote all keys in mappings

Always quote keys in mapping literals.
If you forget to do this, the keys will be interpreted as variables when rendering in Jinja and will evaluate to `undefined`.

Bad:

```
{{ hint({
  id: itemHintId,
  classes: 'nhsuk-checkboxes__hint',
  attributes: item.hint.attributes,
  html: item.hint.html,
  text: item.hint.text
}) }}
```

Good:

```
{{ hint({
  "id": itemHintId,
  "classes": 'nhsuk-checkboxes__hint',
  "attributes": item.hint.attributes,
  "html": item.hint.html,
  "text": item.hint.text
}) }}
```

### Avoid modifying variables inside a loop

When looping over arrays, avoid modifying variables that need to be used outside of the loop.
This does not work in Jinja due to its [scoping behaviour](<https://jinja.palletsprojects.com/en/stable/templates/#builtin-filters:~:text=call_something()%20%25%7D-,Scoping%20Behavior,-Please%20keep%20in>).

Bad:

```
{% set isConditional = false %}
{% for item in items %}
  {% if item.conditional %}
    {% set isConditional = true %}
  {% endif %}
{% endfor %}
```

Good:

```
{% set isConditional = items | selectattr("conditional") | list | length > 0 %}
```

### Avoid strict equality operators

Avoid using the strict equality operators (`===` and `!===`), as they are not compatible with Jinja.

If the type of a value is unknown, `== true` can be safely used in place of `=== true`. This expression is true for a boolean true value or the number `1`, and false for any other values, including strings.

`== false` is weaker than `=== false` and should be avoided. It is true for `false`, `null`, and `undefined` values, but values of `0`, `""`, `[]` or `{}` will yield different results depending on whether you are using Nunjucks or Jinja.

### Avoid Javascript functions

Avoid using Javascript functions directly, as it breaks compatibility with Jinja. Use filters instead.

Bad:

```
{{ items.length }}
```

Good:

```
{{ items | length }}
```

---

Next: [Merging upstream changes](merging-upstream-changes.md)

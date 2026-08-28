# NHS.UK frontend jinja changelog

## 0.10.2

This version is compatible with v10.6.1 of nhsuk-frontend.

### :wrench: **Fixes**

We've made fixes to NHS.UK frontend jinja in the following pull requests:

- [#115: Guard `is escaped` checks with `is defined`](https://github.com/NHSDigital/nhsuk-frontend-jinja/pull/115)

## 0.10.1

This version is compatible with v10.6.1 of nhsuk-frontend.

### :wastebasket: **Deprecated features**

#### Rename the label and legend `"isPageHeading"` option

We've deprecated the `"isPageHeading"` option for labels and legends and added the `"heading"` option.

If you're using any form component macro with the `"isPageHeading"` option, you should:

- rename `"text"` to `"heading"`
- remove `"isPageHeading": true`

```patch
  {{ characterCount({
    "label": {
-     "text": "Can you provide more detail?",
+     "heading": "Can you provide more detail?",
-     "isPageHeading": true,
      "size": "l"
    },
    "name": "more-detail",
    "maxlength": 350,
    "countType": "characters"
  }) }}
```

Other heading options can be configured if necessary. For example, using `heading.id` and `heading.level` when a label acts as an `<h2>` heading for a landmark:

```patch
- <aside>
+ <aside aria-labelledby="search-heading">
    {{ searchInput({
      "label": {
        "text": "Search",
-       "size": "s"
+       "size": "s",
+       "heading": {
+         "id": "search-heading",
+         "level": 2
+       }
      }
    }) }}

    <!-- // … -->
  </aside>
```

For consistency with other components, legends now support the following options:

- `"id"`
- `"caption"`
- `"visuallyHiddenText"`
- `"heading"`
- `"attributes"`

Labels now also support:

- `"caption"`
- `"visuallyHiddenText"`
- `"heading"`

This change was introduced in [pull request #1670: Add label and legend `caption`, `headingLevel` and other options](https://github.com/nhsuk/nhsuk-frontend/pull/1670).

### :recycle: **Changes**

#### Use more options as strings

We added support for alternative string values for labels, legends, hints and error messages in [version 10.6.0](https://github.com/nhsuk/nhsuk-frontend/releases/tag/v10.6.0).

The following component options now support alternative string values:

- Component `"heading"` and `"title"` options
- Card and error summary `"description"` options
- Details `"summary"` option
- Footer `"meta"` and `"copyright"` options
- Image `"caption"` option
- Input `"prefix"` and `"suffix"` options
- Summary list `"key"` and `"value"` options
- Task list `"status"` option
- Table `"head"` and `"rows"` options items

For example, using the table component:

```patch
  {{ table ({
    "caption": "Appointments",
    "firstCellIsHeader": true,
-   "head": [
-     {
-       "text": "Time"
-     },
-     {
-       "text": "Name"
-     },
-     {
-       "text": "Date of birth"
-     }
-   ],
+   "head": ["Time", "Name", "Date of birth"],
-   "rows": [
-     [
-       {
-         "text": "11:00"
-       },
-       {
-         "text": "Laura Stone"
-       },
-       {
-         "text": "4 January 1986"
-       }
-     ],
-     [
-       {
-         "text": "11:30"
-       },
-       {
-         "text": "Emma Katie-Brown"
-       },
-       {
-         "text": "7 February 1976"
-       }
-     ],
-     [
-       {
-         "text": "13:10"
-       },
-       {
-         "text": "David Chen"
-       },
-       {
-         "text": "19 March 1981"
-       }
-     ],
-     [
-       {
-         "text": "13:40"
-       },
-       {
-         "text": "Michael Thompson"
-       },
-       {
-         "text": "6 December 1964"
-       }
-     ],
-     [
-       {
-         "text": "14:20"
-       },
-       {
-         "text": "Juan Martinez"
-       },
-       {
-         "text": "18 April 1975"
-       }
-     ]
-   ]
+   "rows": [
+     ["11:00", "Laura Stone", "4 January 1986"],
+     ["11:30", "Emma Katie-Brown", "7 February 1976"],
+     ["13:10", "David Chen", "19 March 1981"],
+     ["13:40", "Michael Thompson", "6 December 1964"],
+     ["14:20", "Juan Martinez", "18 April 1975"]
+   ]
  }) }}
```

With card and summary list `actions` also supporting arrays of actions items:

```patch
  {{ summaryList({
    "rows": [
-     {
-       "key": {
-         "text": "Name"
-       },
-       "value": {
-         "text": "Karen Francis"
-       },
-       "actions": {
-         "items": [
-           {
-             "href": "#/change",
-             "text": "Change",
-             "visuallyHiddenText": "name"
-           }
-         ]
-       }
-     },
-     {
-       "key": {
-         "text": "Date of birth"
-       },
-       "value": {
-         "text": "15 March 1984"
-       },
-       "actions": {
-         "items": [
-           {
-             "href": "#/change",
-             "text": "Change",
-             "visuallyHiddenText": "date of birth"
-           }
-         ]
-       }
-     }
+     {
+       "key": "Name",
+       "value": "Karen Francis",
+       "actions": [
+         {
+           "href": "#/change",
+           "text": "Change",
+           "visuallyHiddenText": "name"
+         }
+       ]
+     },
+     {
+       "key": "Date of birth",
+       "value": "15 March 1984",
+       "actions": [
+         {
+           "href": "#/change",
+           "text": "Change",
+           "visuallyHiddenText": "date of birth"
+         }
+       ]
+     }
    ]
  }) }}
```

This change was introduced in [pull request #1670: Add label and legend `caption`, `headingLevel` and other options](https://github.com/nhsuk/nhsuk-frontend/pull/1670).

### :wrench: **Fixes**

We've made fixes to NHS.UK frontend in the following pull requests:

- [#2056: Guard against Nunjucks filter errors on `undefined` text](https://github.com/nhsuk/nhsuk-frontend/pull/2056)

## 0.10.0

This version is compatible with v10.6.0 of nhsuk-frontend.

### :new: **New features**

#### Sortable tables

You can now make [table](https://service-manual.nhs.uk/design-system/components/table) columns sortable, so that clicking the header cell sorts the table by that column.

If you're using the `tables` macro, to configure header cells:

- Add the `"sort": "ascending"` or `"sort": "descending"` option to the currently sorted column only
- Add the `"sort": true` option to enable sorting on any other columns
- Add the `"format": "numeric"` option to sort numerically rather than alphabetically

For example:

```patch
  {{ table({
    "caption": "Childhood MMR coverage",
    "head": [
      {
-       "text": "Nation"
+       "text": "Nation",
+       "sort": "ascending"
      },
      {
-       "text": "MMR"
+       "text": "MMR",
+       "format": "numeric",
+       "sort": true
      }
    ],
    "rows": [
      [
        {
          "text": "Northern Ireland"
        },
        {
          "text": "86.4%"
        }
      ],
      [
        {
          "text": "Scotland"
        },
        {
          "text": "89.2%"
        }
      ],
      [
        {
          "text": "Wales"
        },
        {
          "text": "89.5%"
        }
      ]
    ]
  }) }}
```

This was added in [pull request #1969: Add option to make tables sortable](https://github.com/nhsuk/nhsuk-frontend/pull/1654).

#### Scrolling tables

You can now make the [table](https://service-manual.nhs.uk/design-system/components/table) component scrollable, for when your table has many columns and you cannot split it up or use a responsive table.

```patch
  {{ table({
    "caption": "Childhood vaccination coverage",
+   "scroll": true,
    "head": [],
    "rows": []
  }) }}
```

This was added in [pull request #1969: Add option to make tables scroll](https://github.com/nhsuk/nhsuk-frontend/pull/1969).

#### Set table column widths, align text or adjust row borders

We've updated the table component to pass `"align"`, `"href"`, `"visuallyHiddenText"` and `"width"` options to table cells.

For example, to add a column of "Change" links:

```patch
  {{ table({
    "caption": "Appointments",
    "firstCellIsHeader": true,
    "head": [
      {
        "text": "Name",
+       "width": "one-half",
        "sort": "descending"
      },
      {
        "text": "Last log in",
+       "align": "right",
+       "width": "one-third",
        "sort": true
-     }
+     },
+     {
+       "visuallyHiddenText": "Action"
+       "align": "right"
+     }
    ],
    "rows": [
      [
        {
          "text": "Ro Nkosi"
        },
        {
          "text": "28 June 2026"
-       }
+       },
+       {
+         "text": "Change",
+         "visuallyHiddenText": "details for Ro Nkosi",
+         "href": "/change/1111"
+       }
      ],
      [
        {
          "text": "Stellan Park"
        },
        {
          "text": "20 June 2026"
-       }
+       },
+       {
+         "text": "Change",
+         "visuallyHiddenText": "details for Stellan Park",
+         "href": "/change/2222"
+       }
      ]
    ]
  }) }}
```

For consistency with the summary list component, the following boolean options are also available:

- `"border": false` to remove separating borders from all rows
- `"lastRowBorder": false` to remove separating border from the last row

This was added in pull requests [#1654: Add option to make tables sortable](https://github.com/nhsuk/nhsuk-frontend/pull/1654) and [#2025: Align table component options with summary list](https://github.com/nhsuk/nhsuk-frontend/pull/2025).

#### Set summary list widths, IDs and attributes

We've updated the summary list component to pass `"width"`, `"id"` and `"attributes"` options to the key, value and actions items.

Summary list rows also support the `"id"` and `"attributes"` options:

```patch
  {{ summaryList({
    "rows": [
      {
+       "id": "row-1233",
        "key": {
-         "text": "Name"
+         "text": "Name",
+         "width": "one-half"
        },
        "value": {
          "text": "Karen Francis"
        }
      }
    ]
  }) }}
```

This was added in [pull request #2047: Review Nunjucks options for headings and ARIA labels](https://github.com/nhsuk/nhsuk-frontend/pull/2047).

#### Add a modifier class for compact tables

We've added a new `.nhsuk-table--compact` class and `"compact"` option for the [table](https://service-manual.nhs.uk/design-system/components/table) component. This reduces table cell padding at all screen sizes.

```patch
  {{ table({
    "caption": "Childhood vaccination coverage",
+   "compact": true,
    "head": [],
    "rows": []
  }) }}
```

This was added in [pull request #1998: Add compact option for tables](https://github.com/nhsuk/nhsuk-frontend/pull/1998).

#### Add a modifier class for striped tables

We've added a new `.nhsuk-table--striped` class and `"striped"` option for the [table](https://service-manual.nhs.uk/design-system/components/table) component. This adds table row backround colours on alternate rows.

```patch
  {{ table({
    "caption": "Childhood vaccination coverage",
+   "striped": true,
    "head": [],
    "rows": []
  }) }}
```

This was added in [pull request #2003: Add striped option for tables](https://github.com/nhsuk/nhsuk-frontend/pull/2003).

#### Add an "all" option to checkboxes

You can now add an "all" option to checkboxes when JavaScript is available. This gives users the option to quickly select or unselect all the checkboxes.

To use it, add the `"behaviour": "inclusive"` option to a checkbox item. If this checkbox is separated from the others using a divider, add the same option to the divider too:

```patch
  {{ checkboxes({
    "fieldset": {
      "legend": {
        "text": "What are your favourite colours?",
        "size": "l",
        "isPageHeading": true
      }
    },
    "idPrefix": "select-all",
    "name": "example",
    "items": [
+     {
+       "value": "all",
+       "text": "All colours",
+       "behaviour": "inclusive"
+     },
+     {
+       "divider": "or",
+       "behaviour": "inclusive"
+     },
      {
        "value": "red",
        "text": "Red"
      },
      {
        "value": "green",
        "text": "Green"
      },
      {
        "value": "blue",
        "text": "Blue"
      }
    ]
  }) }}
```

This was added in [pull request #1707: Add checkbox "all" option](https://github.com/nhsuk/nhsuk-frontend/pull/1707).

#### Use buttons for card and summary list actions

You can now configure card and summary list actions as button elements, using new macro options:

- `item.id` for the element `id` attribute
- `item.type` for the button `type` attribute
- `item.name` for the button `name` attribute
- `item.value` for the button `value` attribute

Action items without `"href"` will be visually styled as links.

```patch
+ <form method="post" novalidate>
    {{ card({
      "heading": "Regional Manager",
      "actions": {
        "items": [
          {
            "text": "Delete",
-           "href": "/delete"
+           "type": "submit",
+           "name": "action",
+           "value": "delete"
          },
          {
            "text": "Withdraw",
-           "href": "/withdraw",
+           "type": "submit",
+           "name": "action",
+           "value": "withdraw"
          }
        ]
```

This was added in [pull request #1989: Add support for card and summary list actions as buttons](https://github.com/nhsuk/nhsuk-frontend/pull/1989).

#### Use simpler label, legend, hint and error message options

We've updated all form components to support alternative string values for labels, legends, hints and error messages.

For example, when no other nested options are necessary:

```patch
  {{ textarea({
-   "label": {
-     "text": "Can you provide more detail?"
-   },
-   "hint": {
-     "text": "Do not include personal information like your name, date of birth or NHS number"
-   },
+   "label": "Can you provide more detail?",
+   "hint": "Do not include personal information like your name, date of birth or NHS number",
    "name": "more-detail"
  }) }}
```

This was added in [pull request #2047: Review Nunjucks options for headings and ARIA labels](https://github.com/nhsuk/nhsuk-frontend/pull/2047).

#### Review macro `"html"` and `call` usage

For consistency with other components, the following macro changes have been included:

1. Added action link component `caller` support
2. Added back link component `caller` support
3. Added breadcrumb component `item.html` option
4. Added error message component `caller` support
5. Added hint component `caller` support
6. Added image component `caller` support
7. Added skip link component `caller` support
8. Added tag component `caller` support

This was added in [pull request #1999: Add missing `caller` support and fixture coverage to components](https://github.com/nhsuk/nhsuk-frontend/pull/1999).

#### Remove image background colour, bottom border or add custom width

We've updated the image component to add `"background"`, `"border"` and `"width"` options.

These new options can be used to override the defaults. For example, setting `"background": false` and `"border": false` renders the image without a background or bottom border:

```patch
  {{ image({
+   "background": false,
+   "border": false,
    "src": "https://service-manual.nhs.uk/assets/image-example-stretch-marks-600w.jpg",
    "alt": "Close-up of a person's tummy showing a number of creases in the skin under their belly button. Shown on light brown skin."
  }) }}
```

This was added in [pull request #2002: Add image component `background`, `border` and `width` options](https://github.com/nhsuk/nhsuk-frontend/pull/2002).

### :wastebasket: **Deprecated features**

#### Rename checkboxes "none" options

We've renamed the and HTML data attribute options for checkboxes with an option for "none".

If you're using the `checkboxes` macro, you should:

- replace the `"exclusive": true` option with the new `"behaviour": "exclusive"` option
- rename the `"exclusiveGroup"` option to the new `"behaviourGroup"` option

```patch
    "items": [
      {
        "value": "none",
-       "exclusive": true,
-       "exclusiveGroup": "preferences",
+       "behaviour": "exclusive",
+       "behaviourGroup": "preferences"
      }
    ]
```

The previous names are deprecated and will be removed in a future release.

This change was introduced in [pull request #1707: Add checkbox "all" option](https://github.com/nhsuk/nhsuk-frontend/pull/1707).

#### Rename card heading and description options

We've changed the card heading options to support `"text"`, `"html"` and nested options:

- Card `heading` has changed to `heading.text`
- Card `headingHtml` has changed to `heading.html`
- Card `headingClasses` and `headingId` have changed to `heading.classes` and `heading.id`
- Card `headingSize` and `headingLevel` have changed to `heading.size` and `heading.level`
- Card `headingVisuallyHiddenText` has changed to `heading.visuallyHiddenText`

Similarly for description text:

- Card `description` and `descriptionHtml` have changed to `description.text` and `description.html`

```patch
  {{ card({
-   "heading": "Introduction to care and support",
-   "headingSize": "m"
+   "heading": {
+     "text": "Introduction to care and support",
+     "size": "m"
+   },
-   "description": "A quick guide for people who have care and support needs and their carers"
+   "description": {
+     "text": "A quick guide for people who have care and support needs and their carers"
+   }
  }) }}
```

The previous names are deprecated and will be removed in a future release.

This change was introduced in [pull request #2047: Review Nunjucks options for headings and ARIA labels](https://github.com/nhsuk/nhsuk-frontend/pull/2047).

#### Rename details summary options

We've changed the details summary options to support `"text"`, `"html"` and nested options:

- Details `summaryText` has changed to `summary.text`
- Details `summaryHtml` has changed to `summary.html`

```patch
  {{ details({
-   "summaryText": "Where can I find my NHS number?",
+   "summary": {
+     "text": "Where can I find my NHS number?"
+   },
    "html": '<p>An NHS number is a 10 digit number, like <span class="nhsuk-u-nowrap">999 123 4567</span>.</p>'
  }) }}
```

The previous names are deprecated and will be removed in a future release.

This change was introduced in [pull request #2047: Review Nunjucks options for headings and ARIA labels](https://github.com/nhsuk/nhsuk-frontend/pull/2047).

#### Rename error summary title and description options

We've changed the error summary title and description options to support `"text"`, `"html"` and nested options:

- Error summary `titleText` has changed to `heading.text`
- Error summary `titleHtml` has changed to `heading.html`
- Error summary `descriptionText` has changed to `description.text`
- Error summary `descriptionHtml` has changed to `description.html`

```patch
  {{ errorSummary({
-   "titleText": "There is a problem",
+   "heading": {
+     "text": "There is a problem"
+   },
    "errorList": []
  }) }}
```

The previous names are deprecated and will be removed in a future release.

This change was introduced in [pull request #2047: Review Nunjucks options for headings and ARIA labels](https://github.com/nhsuk/nhsuk-frontend/pull/2047).

#### Rename notification banner title options

We've changed the notification banner title options to support `"text"`, `"html"` and nested options:

- Notification banner `titleText` has changed to `title.text`
- Notification banner `titleHtml` has changed to `title.html`
- Notification banner `titleId` has changed to `title.id`
- Notification banner `titleHeadingLevel` has changed to `title.level`
- Notification banner `heading` option has been added

```patch
  {% call notificationBanner({
-   "titleText": "Important"
+   "title": {
+     "text": "Important"
+   },
+   "heading": {
+     "text": "The patient record was updated"
+   }
  }) %}
-   <h3 class="nhsuk-notification-banner__heading">
-     The patient record was updated
-   </h3>
    <p class="nhsuk-body">
      Contact <a class="nhsuk-notification-banner__link" href="#">example@nhs.uk</a> if you think there's a problem.
    </p>
  {% endcall %}
```

The previous names are deprecated and will be removed in a future release.

This change was introduced in [pull request #2047: Review Nunjucks options for headings and ARIA labels](https://github.com/nhsuk/nhsuk-frontend/pull/2047).

#### Rename panel title options

We've changed the panel title options to support `"text"`, `"html"` and nested options:

- Panel `titleText` has changed to `heading.text`
- Panel `titleHtml` has changed to `heading.html`
- Panel `titleSize` has changed to `heading.size`
- Panel `headingLevel` has changed to `heading.level`
- Panel `titleClasses` has changed to `heading.classes`

```patch
  {{ panel({
-   "titleText": "Jodie Brown had a COVID-19 vaccine less than 3 months ago",
-   "titleSize": "l",
+   "heading": {
+     "text": "Jodie Brown had a COVID-19 vaccine less than 3 months ago",
+     "size": "l"
+   },
    "text": "They had a COVID-19 vaccine on 25 September 2025."
  }) }}
```

The previous names are deprecated and will be removed in a future release.

This change was introduced in [pull request #2047: Review Nunjucks options for headings and ARIA labels](https://github.com/nhsuk/nhsuk-frontend/pull/2047).

#### Rename table caption options

We've changed the table caption options to support `"text"`, `"html"` and nested options:

- Table `captionSize` has changed to `caption.size`
- Table `captionClasses` has changed to `caption.classes`

```patch
  {{ table({
-   "caption": "Skin symptoms and possible causes",
-   "captionSize": "l",
+   "caption": {
+     "text": "Skin symptoms and possible causes",
+     "size": "l"
+   },
    "head": [],
    "rows": []
  }) }}
```

The previous names are deprecated and will be removed in a future release.

This change was introduced in [pull request #2047: Review Nunjucks options for headings and ARIA labels](https://github.com/nhsuk/nhsuk-frontend/pull/2047).

#### Rename title and heading options

We've changed the options for titles and headings in all other components to support `text` and `html` and nested options:

- Do and don't list `title` has changed to `heading.text`
- Do and don't list `headingLevel` has changed to `heading.level`
- Footer `navigation.title` has changed to `navigation.heading.text`
- Task list `item.title` has changed to `item.heading`
- Warning callout `headingLevel` has changed to `heading.level`

The previous names are deprecated and will be removed in a future release.

This change was introduced in [pull request #2047: Review Nunjucks options for headings and ARIA labels](https://github.com/nhsuk/nhsuk-frontend/pull/2047).

#### Rename ARIA label and visually hidden text options

We've changed some of the options relating to `aria-label` attributes and visually hidden text. This change makes sure they're named consistently across our components.

- Breadcrumbs `labelText` has changed to `ariaLabel`
- Contents list `landmarkLabel` has changed to `ariaLabel`
- Footer `meta.visuallyHiddenTitle` has changed to `meta.visuallyHiddenText`
- Header `search.placeholder` has changed to `search.input.placeholder`
- Header `search.visuallyHiddenLabel` has changed to `search.label.visuallyHiddenText`
- Header `search.visuallyHiddenButton` has changed to `search.button.ariaLabel`
- Pagination `item.visuallyHiddenText` has changed to `item.ariaLabel`
- Pagination `landmarkLabel` has changed to `ariaLabel`
- Pagination `previous.labelText` has changed to `previous.label.text`
- Pagination `next.labelText` has changed to `next.label.text`
- Password input `showPasswordAriaLabelText` has changed to `showPasswordAriaLabel`
- Password input `hidePasswordAriaLabelText` has changed to `hidePasswordAriaLabel`
- Tabs `title` has changed to `visuallyHiddenText`

For options with `"text"` and `"html"` nested options, alternative string values are also supported:

```patch
  {{ pagination({
    "previous": {
-     "label": {
-       "text": "Treatments"
-     },
+     "label": "Treatments",
      "href": "/section/treatments"
    },
    "next": {
-     "label": {
-       "text": "Symptoms"
-     },
+     "label": "Symptoms",
      "href": "/section/symptoms"
    }
  }) }}
```

The previous names are deprecated and will be removed in a future release.

This change was introduced in [pull request #2047: Review Nunjucks options for headings and ARIA labels](https://github.com/nhsuk/nhsuk-frontend/pull/2047).

#### Rename reverse and responsive table HTML classes

We've renamed HTML classes for reverse and responsive tables. You can still use the previous names but we'll remove them in a future breaking release.

If you're using the `table` macro with the `"responsive"` option, you should:

- remove the unnecessary `"header"` option from table `"rows"` nested items

```patch
  "rows": [
    [
      {
-       "header": "Age",
        "text": "3 to 5 months (weighing more than 5kg)"
      },
      {
-       "header": "How much?",
        "text": "2.5ml"
      },
      {
-       "header": "How often?",
        "text": "Max 3 times in 24 hours"
      }
    ],
```

This change was introduced in pull requests [#1998: Add `compact` option for tables](https://github.com/nhsuk/nhsuk-frontend/pull/1998) and [#2003: Add `striped` option for tables](https://github.com/nhsuk/nhsuk-frontend/pull/2003).

#### Stop using the `"element"` option on action links, back links and buttons

We’ve deprecated the `"element"` option for action links, back links and button components.

In a future release, if the `"href"` option is set the component will automatically use the `<a>` element. If the `"href"` option is not set the component will automatically use the `<button>` element. It will not be possible to override this change.

```patch
  {{ actionLink({
    "text": "Action link",
-   "element": "button"
+   "type": "submit"
  }) }}
```

This change was introduced in [pull request #2047: Review Nunjucks options for headings and ARIA labels](https://github.com/nhsuk/nhsuk-frontend/pull/2047).

## 0.9.1

This version is compatible with v10.5.2 of nhsuk-frontend.

### :wrench: **Fixes**

- [#103: Add new icons from NHS.UK frontend](https://github.com/NHSDigital/nhsuk-frontend-jinja/pull/103)

## 0.9.0

This version is compatible with v10.5.0 of nhsuk-frontend.

### :new: **New features**

#### New search input component

We've added a new [search input component](https://service-manual.nhs.uk/design-system/components/search-input).

To use the `searchInput` macro in your service:

```njk
{{ searchInput({
  "label": {
    "text": "Find session"
  },
  "name": "search",
  "width": 10
}) }}
```

This change was introduced in [pull request #1660: Add search input component](https://github.com/nhsuk/nhsuk-frontend/pull/1660).

#### Improved character count counting

We've added a new `"countType"` option to the character count component to enable [improved counting with `Intl.Segmenter`](https://developer.mozilla.org/en-US/blog/javascript-intl-segmenter-i18n/).

This feature was introduced because [JavaScript counts `String: length` in code units](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String/length) not characters, for example:

| String | Length | Remarks                                                                    |
| ------ | ------ | -------------------------------------------------------------------------- |
| cafȩ́   | 5      | The character `ȩ́` counted as 2 code units                                  |
| cafȩ́   | 5      | The character `ȩ` with combining mark ` ́` counted as 2 code units          |
| cafȩ́   | 6      | The character `e` with combining marks ` ́` and ` ̧` counted as 3 code units |
| 😹     | 2      | The cat emoji counted as 2 code units                                      |
| 👩🏻‍🚀     | 7      | The astronaut emoji with gender and skin modifiers counted as 7 code units |

Similarly when counting words, "my mother-in-law" is now counted as 4 (not 2) words to correctly follow the [Unicode **Default Word Boundary Specification**](https://unicode.org/reports/tr29/#Default_Word_Boundaries).

To enable improved counting in [supported browsers](https://caniuse.com/wf-intl-segmenter) you should either:

- add `"countType": "characters"` to count user-perceived characters
- add `"countType": "words"` to count words between word boundaries

Unsupported browsers will default to the `"textareaDescriptionText"` message shown when JavaScript is unavailable, such as:

> You can enter up to 350 characters

When counting characters:

```patch
  {{ characterCount({
    "label": {
      "text": "Can you provide more detail?",
      "size": "l",
      "isPageHeading": true
    },
    "name": "more-detail",
-   "maxlength": 350
+   "maxlength": 350,
+   "countType": "characters"
  }) }}
```

Or when counting words:

```patch
  {{ characterCount({
    "label": {
      "text": "Can you provide more detail?",
      "size": "l",
      "isPageHeading": true
    },
    "name": "more-detail",
-   "maxwords": 150
+   "maxlength": 150,
+   "countType": "words"
  }) }}
```

Note: [The character count `"maxwords"` option and word counting behaviour are deprecated](#rename-the-character-count-maxwords-option) and will be removed in a future release. You must replace `"maxwords"` with `"maxlength"` when using `"countType": "words"`.

This was added in pull requests [#1892: Refactor character count method to reduce repeated updates](https://github.com/nhsuk/nhsuk-frontend/pull/1892), [#1893: Deprecate character count `maxwords` and add `countType` option](https://github.com/nhsuk/nhsuk-frontend/pull/1893), [#1895: Add character count `countType: "characters"` option using Intl.Segmenter](https://github.com/nhsuk/nhsuk-frontend/pull/1895) and [#1899: Add character count `countType: "words"` option using Intl.Segmenter](https://github.com/nhsuk/nhsuk-frontend/pull/1899).

#### Add date input `"day"`, `"month"` and `"year"` options

We've updated the date input component to add individual `"day"`, `"month"` and `"year"` options.

These new options can be used to partially override the defaults. For example, setting `"error": true` on the year item no longer requires all other item defaults to be set:

```patch
  {{ dateInput({
    "fieldset": {
      "legend": {
        "text": "What is your date of birth?",
        "size": "l",
        "isPageHeading": true
      }
    },
    "errorMessage": {
      "text": "Date of birth must include a year"
    },
    "namePrefix": "dob",
    "values": data.dob,
-   "items": [
-     {
-       "name": "day",
-       "label": "Day",
-       "width": 2
-     },
-     {
-       "name": "month",
-       "label": "Month",
-       "width": 2
-     },
-     {
-       "name": "year",
-       "label": "Year",
-       "width": 4,
-       "error": true
-     }
-   ]
+   "year": {
+     "error": true
+   }
  }) }}
```

This was added in [pull request #1869: Add date input `day`, `month` and `year` options](https://github.com/nhsuk/nhsuk-frontend/pull/1869).

#### Updated macro options for components

For consistency with other components, we’ve added new macro options:

- Action link `element` and `type` options
- Back link `type` option
- Character count `autocomplete` option
- Checkboxes and radios `formGroup.classes` option
- Date input and password input `inputWrapper` option
- Password input `code`, `prefix` and `suffix` options
- Password input button `variant` option
- Radios `formGroup.classes` option

Visit the [design system in the NHS digital service manual](https://service-manual.nhs.uk/design-system/components) to see options for each component.

This was added in pull requests [#1916: Add disabled component examples and review Nunjucks options](https://github.com/nhsuk/nhsuk-frontend/pull/1916) and [#1946: Updates to link classes and mixins, support for action link as a button](https://github.com/nhsuk/nhsuk-frontend/pull/1946).

#### Added a top-level `"disabled"` option to more form controls

We’ve updated more components to include a top-level `"disabled"` option. This will make it easier to set the disabled state for these form controls.

- Character count `disabled` option
- Checkboxes and radios `disabled` option
- Date input `disabled` option
- Password input `disabled` option

Disabled form controls have poor contrast and can confuse some users, so avoid them if possible.

Only use disabled form controls if research shows it makes the user interface easier to understand.

This was added in [pull request #1916: Add disabled component examples and review Nunjucks options](https://github.com/nhsuk/nhsuk-frontend/pull/1916).

#### Add icons to buttons

You can now [add icons](https://service-manual.nhs.uk/design-system/styles/icons) to buttons using the `"icon"` options.

For example, using `"icon": "search"` to add an icon-only search button to a text input:

```njk
{{ input({
  "formGroup": {
    "afterInput": {
      "html": button({
        "ariaLabel": "Find",
        "icon": "search",
        "small": true
      })
    }
  }
}) }}
```

With support for both an icon and text shown together:

```patch
  "html": button({
-   "ariaLabel": "Find",
+   "text": "Find",
    "icon": "search",
    "small": true
  })
```

Or to change the icon and adjust placement:

```patch
 "html": button({
   "text": "Find",
-   "icon": "search",
+   "icon": {
+     "name": "arrow-right",
+     "placement": "end"
+   }
 })
```

This was added in [pull request #1712: Add support for icon buttons](https://github.com/nhsuk/nhsuk-frontend/pull/1712).

#### Add a modifier class for inline checkboxes

We've added a new `.nhsuk-checkboxes--inline` class and `"inline"` option for the [checkboxes](https://service-manual.nhs.uk/design-system/components/header) component.

If there are only 2 short options, you can use this to display the checkboxes horizontally (inline). On small screens such as mobile devices, the checkboxes will still stack vertically.

For example:

```patch
  {{ checkboxes({
    "fieldset": {
      "legend": {
        "text": "Which nipple has changed?"
      }
    },
    "name": "area",
+   "inline": true,
    "items": [
      {
        "value": "right",
        "text": "Right nipple"
      },
      {
        "value": "left",
        "text": "Left nipple"
      }
    ]
  }) }}
```

This was added in [pull request #1937: Add a modifier class for inline checkboxes](https://github.com/nhsuk/nhsuk-frontend/pull/1937).

#### Add a template with all components imported

If you are using our [page template](https://service-manual.nhs.uk/design-system/styles/page-template), you can now extend `template-with-imports.jinja` instead of `template.jinja` to automatically import all components.

This was added in [pull request #1921: Add a template with all components imported](https://github.com/nhsuk/nhsuk-frontend/pull/1921).

### :wastebasket: **Deprecated features**

#### Rename the character count `"maxwords"` option

To support improved word counting using the browser [`Intl.Segmenter` API](https://developer.mozilla.org/en-US/blog/javascript-intl-segmenter-i18n/), you should replace the character count `"maxwords"` option with `"maxlength"` and set `"countType": "words"`.

For example, using Jinja:

```patch
  {{ characterCount({
    "label": {
      "text": "Can you provide more detail?",
      "size": "l",
      "isPageHeading": true
    },
    "name": "more-detail",
-   "maxwords": 150
+   "maxlength": 150,
+   "countType": "words"
  }) }}
```

Or when using the JavaScript API:

```patch
  new CharacterCount($root, {
-   maxwords: 150
+   maxlength: 150,
+   countType: 'words'
  })
```

The previous `"maxwords"` option and word counting behaviour are deprecated and will be removed in a future release.

This change was introduced in pull requests [#1893: Deprecate character count `maxwords` and add `countType` option](https://github.com/nhsuk/nhsuk-frontend/pull/1893) and [#1899: Add character count `countType: "words"` option using Intl.Segmenter](https://github.com/nhsuk/nhsuk-frontend/pull/1899).

## 0.8.0

This version is compatible with v10.4.0 of nhsuk-frontend.

### :new: **New features**

#### Add a modifier class for header inline search or account links

We've added a new `.nhsuk-header--inline` class and `"inline"` macro option for the [header](https://service-manual.nhs.uk/design-system/components/header) component. This positions the search bar (or account links) inline with the NHS logo on small screens, depending on the length of your service name. For example:

```patch
  {{ header({
+   "inline": true,
    "account": {
      "items": [
        {
          "text": "Log in",
          "href": "/log-in"
        }
      ]
    }
  }) }}
```

This was added in pull requests [#1783: Add support for inline header search or account](https://github.com/nhsuk/nhsuk-frontend/pull/1783) and [#1801: Add Nunjucks options for components with modifier classes](https://github.com/nhsuk/nhsuk-frontend/pull/1801).

#### Add macro options for components with modifier classes

We've added a new `"variant"` macro option to action links, back links, buttons, breadcrumbs, panels and tables as a simpler alternative to the variant modifier classes. For example:

```patch
  {{ button({
    "text": "Yes, delete this vaccine",
-   "classes": "nhsuk-button--warning"
+   "variant": "warning"
  }) }}
```

For modifiers that can exist together, these are now supported using boolean options, for example:

```patch
  {{ "radios"({
    "fieldset": {
      "legend": {
        "text": "Sort by"
      }
    },
-   "classes": "nhsuk-radios--small nhsuk-radios--inline",
+   "small": true,
+   "inline": true,
```

With the following boolean options now available:

- Button, checkboxes and radios with `"small": true`
- Date input items with `"error": true`
- Radios with `"inline": true`
- Header navigation with `"justified": true`
- Summary lists with `"lastRowBorder": false`
- Summary lists (and rows) with `"border": false`
- Tags with `"border": false`
- Text input with `"code": true`

We've also added the `"width"` option to text and date input items as a simpler alternative to the [fixed width classes](https://service-manual.nhs.uk/design-system/components/text-input#fixed-width-inputs), for example:

```patch
  "items": [
    {
      "name": "day",
-     "classes": "nhsuk-input--width-2"
+     "width": 2
    },
    {
      "name": "month",
-     "classes": "nhsuk-input--width-2"
+     "width": 2
    },
    {
      "name": "year",
-     "classes": "nhsuk-input--width-4"
+     "width": 4
    }
  ]
```

Or with both boolean and width modifiers set together:

```patch
  {{ input({
    "label": {
      "text": "NHS number"
    },
-   "classes": "nhsuk-input--width-10 nhsuk-input--code",
+   "width": 10,
+   "code": true,
    "inputmode": "numeric",
    "spellcheck": false
  }) }}
```

We've also added the `"colour"` option to the tag component as a simpler way to set a colour:

```patch
  {{ tag({
    "text": "Delayed",
-   "classes": "nhsuk-tag--yellow"
+   "colour": "yellow"
  }) }}
```

This was added in [pull request #1801: Add Nunjucks options for components with modifier classes](https://github.com/nhsuk/nhsuk-frontend/pull/1801).

### :wastebasket: **Deprecated features**

#### Rename macro macro options for component variants

All component variants now use the new `"variant"` macro option so we've deprecated the `"type"` and boolean options for cards, notification banners and do and don't lists.

If you're using the `card` macro:

- replace the `"feature": true` option with `"variant": "feature"`
- replace the `"primary": true` option with `"variant": "primary"`
- replace the `"secondary": true` option with `"variant": "secondary"`
- replace the `"warning": true` option with `"variant": "warning"`
- replace the `"type": "non-urgent"` option with `"variant": "non-urgent"`
- replace the `"type": "urgent"` option with `"variant": "urgent"`
- replace the `"type": "emergency"` option with `"variant": "emergency"`

If you're using the `notificationBanner` macro:

- replace the `"type": "success"` option with `"variant": "success"`

If you're using the `list` macro:

- replace the `"type": "tick"` option with `"icon": "tick"`
- replace the `"type": "cross"` option with `"icon": "cross"`

The previous names are deprecated and will be removed in a future release.

## 0.7.2

### :wrench: **Fixes**

- [#1797: Ensure input passes label.id down to the label](https://github.com/nhsuk/nhsuk-frontend/pull/1797)

## 0.7.1

### :wrench: **Fixes**

- fix attributes sometimes being ignored if they have a value of 0

## 0.7.0

This version is compatible with v10.3.0 of nhsuk-frontend.

### :new: **New features**

#### New file upload component

We've added a new [file upload component](https://service-manual.nhs.uk/design-system/components/file-upload) which:

- makes the file inputs easier to use for drag and drop
- allows the text of the component to be translated
- fixes accessibility issues for users of Dragon, a speech recognition software

To use the `fileUpload` macro in your service:

```jinja
{{ fileUpload({
  "label": {
    "text": "Upload your photo"
  }
  "id": "file-upload",
  "name": "photo"
}) }}
```

If you're importing components individually in your JavaScript, which we recommend for better performance, you'll then need to import and initialise the new `FileUpload` component.

```mjs
import { createAll, FileUpload } from 'nhsuk-frontend'

createAll(FileUpload)
```

This change was introduced in [pull request #1556: Uplift GOV.UK Frontend file upload component](https://github.com/nhsuk/nhsuk-frontend/pull/1556)

#### Interruption panel

We've added a new variant of the panel component with a solid blue background and white text. This can be used as an interruption card.

This was added in [pull request #1196: Add interruption panel variant](https://github.com/nhsuk/nhsuk-frontend/pull/1196).

#### Use cards to visually separate multiple summary lists on a single page

You can now wrap a [card](https://service-manual.nhs.uk/design-system/components/cards) around [summary lists](https://service-manual.nhs.uk/design-system/components/summary-list) to help you:

- design and build pages with multiple summary lists
- show visual dividers between summary lists
- allow users to apply actions to entire lists

This was added in [pull request #1685: Add card enhancement to summary list](https://github.com/nhsuk/nhsuk-frontend/pull/1685).

### :wastebasket: **Deprecated features**

#### Rename macro options for images

For consistency with other components, macro options for images have changed. The previous names are deprecated and will be removed in a future release.

If you're using the `card` macro with the `imgURL` or `imgALT` options in your service, you should:

- replace the `imgURL` option with the nested `image.src` option
- replace the `imgALT` option with the nested `image.alt` option

```patch
  {{ card({
-   "imgURL": "https://service-manual.nhs.uk/assets/blog-prototype-kit.png",
-   "imgALT": "Illustration showing icons, design system components and a terminal app. Each one follows a dotted line into a laptop to become a prototype.",
+   "image": {
+     "src": "https://service-manual.nhs.uk/assets/blog-prototype-kit.png",
+     "alt": "Illustration showing icons, design system components and a terminal app. Each one follows a dotted line into a laptop to become a prototype."
+   },
    "heading": "Why we are reinvesting in the NHS prototype kit"
  }) }}
```

If you're using the `hero` macro with the `imageURL` option in your service, you should:

- replace the `imageURL` option with the nested `image.src` option

```patch
  {{ hero({
-   "imageURL": "https://service-manual.nhs.uk/assets/blog-prototype-kit.png"
+   "image": {
+     "src": "https://service-manual.nhs.uk/assets/blog-prototype-kit.png"
+   }
  }) }}
```

If you're using the `image` macro with the `caption` option in your service, you should:

- replace the `caption` option with the nested `caption.text` option

```patch
  {{ image({
    "src": "https://service-manual.nhs.uk/assets/image-example-stretch-marks-600w.jpg",
    "alt": "Close-up of a person's tummy showing a number of creases in the skin under their belly button. Shown on light brown skin.",
-   "caption": "Stretch marks can be pink, red, brown, black, silver or purple. They usually start off darker and fade over time."
+   "caption": {
+     "text": "Stretch marks can be pink, red, brown, black, silver or purple. They usually start off darker and fade over time."
+   }
  }) }}
```

This change was introduced in [pull request #1763: Review Nunjucks params for header search and images](https://github.com/nhsuk/nhsuk-frontend/pull/1763).

#### Update the HTML for tables as a panel

For consistency with other components, the options for tables as a panel have changed. The previous names are deprecated and will be removed in a future release.

If you're using the `table` macro with the `panel` option, you should migrate to the feature card enhancement:

- replace the `heading` option with the nested `card.heading` option
- replace the `headingLevel` option with the nested `card.headingLevel` option
- replace the `panel` option with the nested `card.feature` option
- replace the `panelClasses` option with the nested `card.classes` option
- replace the `tableClasses` option with the `classes` option

```patch
  {{ table({
-   "heading": "Skin symptoms and possible causes",
-   "headingLevel": 3,
-   "panel": true,
-   "panelClasses": "nhsuk-u-margin-bottom-8",
+   "card": {
+     "heading": "Skin symptoms and possible causes",
+     "headingLevel": 3,
+     "feature": true,
+     "classes": "nhsuk-u-margin-bottom-8"
+   },
-   "tableClasses": "nhsuk-u-margin-bottom-0",
+   "classes": "nhsuk-u-margin-bottom-0",
    "head": [],
    "rows": []
  }) }}
```

This change was introduced in [pull request #1685: Add card enhancements to summary list, table and warning callout](https://github.com/nhsuk/nhsuk-frontend/pull/1685).

## 0.6.1

- Fix regression that caused extra `aria-describedby` attributes to be emitted with empty values.

## 0.6.0

- Supports [nhsuk-frontend v10.2.0](https://github.com/nhsuk/nhsuk-frontend/compare/v10.1.0...v10.2.0).
- See the [nhsuk-frontend changelog](https://github.com/nhsuk/nhsuk-frontend/blob/main/CHANGELOG.md) for further details.

### :new: **New features**

#### Use the password input component to help users accessibly enter passwords

The [password input component](https://service-manual.nhs.uk/design-system/components/password-input) allows users to choose:

- whether their passwords are visible or not
- to enter their passwords in plain text

This helps users use longer and more complex passwords without needing to remember what they've already typed.

#### Smaller versions of buttons

You can now use smaller versions of [buttons](https://service-manual.nhs.uk/design-system/components/buttons) by adding the `nhsuk-button--small` class.

#### Add inline buttons to text inputs and select menus

You can now add inline buttons to text inputs and select menus using the `formGroup.afterInput` options.

```jinja
{{ input({
  formGroup: {
    "afterInput": {
      "html": button({
        "text": "Search",
        "classes": "nhsuk-button--small"
      })
    }
  }
}) }}
```

#### Updated macro options for nested items

For consistency with other components with nested items, we’ve added new macro options:

- Action link and skip link `html` option
- Checkboxes and radios item `classes` option
- Contents list item `html`, `classes` and `attributes` options
- Summary list action item `classes` and `attributes` options

#### Add a modifier class for text input styles that accept codes and sequences

We've added a new `.nhsuk-input--code` class for the [text input](https://service-manual.nhs.uk/design-system/components/text-input) component. This improves readability of text inputs that receive codes and sequences (like NHS numbers, security codes or booking references).

You can add it through the classes option to the macro.

#### Add a 'divider' option to selects

Newer browsers support [using `<hr>` (horizontal rule) elements inside a `<select>` element](https://developer.chrome.com/blog/hr-in-select/) to help visually break up options for better readability.

We've added a new `divider` option on select items to support this feature. For example:

```jinja
{{ select({
  "label": {
    "text": "Sort by"
  },
  "name": 'sort',
  "items": [
    {
      "value": "first-name-ascending",
      "text": "First name (A to Z)"
    },
    {
      "value": "first-name-descending",
      "text": "First name (Z to A)"
    },
    {
      "divider": true
    },
    {
      "value": "last-name-ascending",
      "text": "Last name (A to Z)"
    },
    {
      "value": "last-name-descending",
      "text": "Last name (Z to A)"
    }
  ]
}
}) }}
```

#### Add a 'size' option to labels and legends

We've added a new `size` option to labels and legends as a simpler alternative to the size modifier classes. For example:

```patch
  {{ input({
    "label": {
      "text": 'What is your full name?',
-     "classes": "nhsuk-label--l"
+     "size": "l"
    }
  }) }}
```

```patch
  {{ radios({
    "fieldset": {
      "legend": {
        "text": "How do you want to be contacted about this?",
-       "classes": "nhsuk-fieldset__legend--l"
+       "size": "l"
      }
    },
    "items": []
  }}
```

#### Add a 'captionSize' option to tables

We've added a new `captionSize` option to tables as a simpler alternative to the caption modifier classes. For example:

```patch
  {{ table({
    "caption": "Skin symptoms and possible causes",
-   "captionClasses": "nhsuk-table__caption--l",
+   "captionSize": "l",
    "rows": []
  }) }}
```

## 0.5.0

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

```jinja
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

```jinja
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

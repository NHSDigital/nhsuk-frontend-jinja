def test_string_values(environment):
    template = (
        '{% from "nhsuk/macros/attributes.jinja" import nhsukAttributes %}\n'
        + '<div{{ nhsukAttributes({"a": "Value A", "b": "Value B"}) }}></div>'
    )

    result = environment.from_string(template).render()
    assert result == '<div a="Value A" b="Value B"></div>'


def test_string_values_mapping(environment):
    template = (
        '{% from "nhsuk/macros/attributes.jinja" import nhsukAttributes %}\n'
        + '<div{{ nhsukAttributes({"a": {"value": "Value A" }, "b": {"value": "Value B" }}) }}></div>'
    )

    result = environment.from_string(template).render()
    assert result == '<div a="Value A" b="Value B"></div>'


def test_string_values_safe(environment):
    template = """
        {%- from "nhsuk/macros/attributes.jinja" import nhsukAttributes -%}

        <div {{- nhsukAttributes({
          "data-text": "Testing",
          "data-unsafe-text": "Testing & more",
          "data-safe-text": "Testing &amp; more" | safe,
          "data-escaped-text": "Testing & more" | escape,
          "data-double-escaped-text": "Testing &amp; more" | escape
        }) }}></div>
    """

    result = environment.from_string(template).render().strip()
    assert (
        result
        == '<div data-text="Testing" data-unsafe-text="Testing &amp; more" data-safe-text="Testing &amp; more" data-escaped-text="Testing &amp; more" data-double-escaped-text="Testing &amp;amp; more"></div>'
    )


def test_string_values_safe_mapping(environment):
    template = """
        {%- from "nhsuk/macros/attributes.jinja" import nhsukAttributes -%}

        <div {{- nhsukAttributes({
          "data-text": {
            "value": "Testing"
          },
          "data-unsafe-text": {
            "value": "Testing & more"
          },
          "data-safe-text": {
            "value": "Testing &amp; more" | safe
          },
          "data-escaped-text": {
            "value": "Testing & more" | escape
          },
          "data-double-escaped-text": {
            "value": "Testing &amp; more" | escape
          }
        }) }}></div>
    """

    result = environment.from_string(template).render().strip()
    assert (
        result
        == '<div data-text="Testing" data-unsafe-text="Testing &amp; more" data-safe-text="Testing &amp; more" data-escaped-text="Testing &amp; more" data-double-escaped-text="Testing &amp;amp; more"></div>'
    )


def test_string_only(environment):
    template = (
        '{% from "nhsuk/macros/attributes.jinja" import nhsukAttributes %}\n'
        + '<div{{ nhsukAttributes(\' a="Value A" b="Value B"\') }}></div>'
    )

    result = environment.from_string(template).render()
    assert result == '<div a="Value A" b="Value B"></div>'


def test_string_only_safe(environment):
    template = (
        '{% from "nhsuk/macros/attributes.jinja" import nhsukAttributes %}\n'
        + '<div{{ nhsukAttributes(\' a="Value A" b="Value B"\' | safe) }}></div>'
    )

    result = environment.from_string(template).render()
    assert result == '<div a="Value A" b="Value B"></div>'


def test_nullish_values(environment):
    template = """
        {%- from "nhsuk/macros/attributes.jinja" import nhsukAttributes -%}

        <div {{- nhsukAttributes({
          "a": undefined,
          "b": null,
          "c": None,
          "d": "",
          "e": 0,
          "f": False
        }) }}></div>
    """

    result = environment.from_string(template).render().strip()
    assert result == '<div a="" b="" c="" d="" e="0" f="false"></div>'


def test_nullish_values_mapping(environment):
    template = """
        {%- from "nhsuk/macros/attributes.jinja" import nhsukAttributes -%}

        <div {{- nhsukAttributes({
          "a": {
            "value": undefined,
            "optional": False
          },
          "b": {
            "value": null,
            "optional": False
          },
          "c": {
            "value": None,
            "optional": False
          },
          "d": {
            "value": "",
            "optional": False
          },
          "e": {
            "value": 0,
            "optional": False
          },
          "f": {
            "value": False,
            "optional": False
          }
        }) }}></div>
    """

    result = environment.from_string(template).render().strip()
    assert result == '<div a="" b="" c="" d="" e="0" f="false"></div>'


def test_boolean_values_lowercase(environment):
    template = (
        '{% from "nhsuk/macros/attributes.jinja" import nhsukAttributes %}\n'
        + '<div{{ nhsukAttributes({"a": True, "b": False}) }}></div>'
    )

    result = environment.from_string(template).render()
    assert result == '<div a="true" b="false"></div>'


def test_optional_true_renders_name_only(environment):
    template = (
        '{% from "nhsuk/macros/attributes.jinja" import nhsukAttributes %}\n'
        + '<div{{ nhsukAttributes({"a": {"optional": True, "value": True}, "b": "abc"}) }}></div>'
    )

    result = environment.from_string(template).render()
    assert result == '<div a b="abc"></div>'


def test_optional_false_is_ommitted(environment):
    template = (
        '{% from "nhsuk/macros/attributes.jinja" import nhsukAttributes %}\n'
        + '<div{{ nhsukAttributes({"a": {"optional": True, "value": False}, "b": "abc"}) }}></div>'
    )

    result = environment.from_string(template).render()
    assert result == '<div b="abc"></div>'


def test_optional_none_is_ommitted(environment):
    template = (
        '{% from "nhsuk/macros/attributes.jinja" import nhsukAttributes %}\n'
        + '<div{{ nhsukAttributes({"a": {"optional": True, "value": none}, "b": "abc"}) }}></div>'
    )

    result = environment.from_string(template).render()
    assert result == '<div b="abc"></div>'


def test_optional_undefined_is_ommitted(environment):
    template = (
        '{% from "nhsuk/macros/attributes.jinja" import nhsukAttributes %}\n'
        + '<div{{ nhsukAttributes({"a": {"optional": True, "value": undefined}, "b": "abc"}) }}></div>'
    )

    result = environment.from_string(template).render()
    assert result == '<div b="abc"></div>'


def test_optional_empty_string_renders_value(environment):
    template = (
        '{% from "nhsuk/macros/attributes.jinja" import nhsukAttributes %}\n'
        + '<div{{ nhsukAttributes({"a": {"optional": True, "value": ""}, "b": "abc"}) }}></div>'
    )

    result = environment.from_string(template).render()
    assert result == '<div a="" b="abc"></div>'


def test_optional_safe_string_renders_value(environment):
    template = (
        '{% from "nhsuk/macros/attributes.jinja" import nhsukAttributes %}\n'
        + '<div{{ nhsukAttributes({"a": {"optional": True, "value": "a &amp; b" | safe}, "b": "abc"}) }}></div>'
    )

    result = environment.from_string(template).render()
    assert result == '<div a="a &amp; b" b="abc"></div>'


def test_empty_attributes(environment):
    template = (
        '{% from "nhsuk/macros/attributes.jinja" import nhsukAttributes %}\n'
        + "<div{{ nhsukAttributes({}) }}></div>"
    )

    result = environment.from_string(template).render()
    assert result == "<div></div>"

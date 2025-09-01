def test_multiple_attributes(environment):
    template = (
        '{% from "nhsuk/macros/attributes.jinja" import nhsukAttributes %}\n'
        + '<div{{ nhsukAttributes({"a": "a-value", "b": "b-value"}) }}></div>'
    )

    result = environment.from_string(template).render()
    assert result == '<div a="a-value" b="b-value"></div>'


def test_conditional_true_renders_name_only(environment):
    template = (
        '{% from "nhsuk/macros/attributes.jinja" import nhsukAttributes %}\n'
        + '<div{{ nhsukAttributes({"a": {"optional": True, "value": True}, "b": "abc"}) }}></div>'
    )

    result = environment.from_string(template).render()
    assert result == '<div a b="abc"></div>'


def test_conditional_false_is_ommitted(environment):
    template = (
        '{% from "nhsuk/macros/attributes.jinja" import nhsukAttributes %}\n'
        + '<div{{ nhsukAttributes({"a": {"optional": True, "value": False}, "b": "abc"}) }}></div>'
    )

    result = environment.from_string(template).render()
    assert result == '<div b="abc"></div>'


def test_empty_attributes(environment):
    template = (
        '{% from "nhsuk/macros/attributes.jinja" import nhsukAttributes %}\n'
        + "<div{{ nhsukAttributes({}) }}></div>"
    )

    result = environment.from_string(template).render()
    assert result == "<div></div>"


def test_safe_value_does_not_get_double_escaped(environment):
    template = (
        '{% from "nhsuk/macros/attributes.jinja" import nhsukAttributes %}\n'
        + '<div{{ nhsukAttributes({"a": "&amp;" | safe}) }}></div>'
    )
    result = environment.from_string(template).render()
    assert result == '<div a="&amp;"></div>'

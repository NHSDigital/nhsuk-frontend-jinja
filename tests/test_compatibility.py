"""
Test HTML-compatibility with NHS.UK frontend
"""

import difflib
import json
from pathlib import Path

import pytest
from bs4 import BeautifulSoup

from .fixture_loader import FixtureLoader

ROOT = Path(__file__).parent.parent

FIXTURE_LOADER = FixtureLoader()


def camel_case(kebab_case):
    """
    turn kebab-case into camelCase
    """
    parts = kebab_case.split("-")
    return parts[0] + "".join([s.title() for s in parts[1:]])


def render(environment, component, options, call_content):
    """
    Generate a template that renders a component, and return the rendered result

    If call_content is provided, a call block is used, otherwise a regular macro call
    is used.
    """
    component_camel_case = camel_case(component)
    if component in ("tables", "images"):
        component_camel_case = component_camel_case[:-1]
    elif component == "do-dont-list":
        component_camel_case = "list"

    options_json = json.dumps(options)

    if call_content:
        template_string = f"{{% from 'nhsuk/components/{component}/macro.jinja' import {component_camel_case}%}}\n{{% call {component_camel_case}({options_json}) %}}{call_content}{{% endcall %}}"
    else:
        template_string = f"{{% from 'nhsuk/components/{component}/macro.jinja' import {component_camel_case}%}}\n{{{{ {component_camel_case}({options_json}) }}}}"

    result = environment.from_string(template_string).render()
    return result


@pytest.mark.parametrize("component,fixture_name", FIXTURE_LOADER.fixture_keys)
def test_compatibility(environment, component, fixture_name):
    ideal = FIXTURE_LOADER.expected_html(component, fixture_name)
    options = FIXTURE_LOADER.options(component, fixture_name)
    actual = render(
        environment,
        component,
        options,
        FIXTURE_LOADER.call_content(component, fixture_name),
    )

    # We are not currently matching the nunjucks version on whitespace, so test
    # a prettified version.
    ideal_formatted = BeautifulSoup(ideal, features="html.parser").prettify()
    actual_formatted = BeautifulSoup(actual, features="html.parser").prettify()

    assert actual_formatted == ideal_formatted, difflib.context_diff(
        actual_formatted, ideal_formatted
    )

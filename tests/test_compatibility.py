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


@pytest.mark.parametrize("component", FIXTURE_LOADER.components)
def test_compatibility(environment, component, subtests):
    for fixture_name, fixture in FIXTURE_LOADER.fixtures(component):
        with subtests.test(msg=f"{component}: {fixture_name}"):
            ideal = fixture.expected
            options = fixture.options

            actual = render(
                environment,
                component,
                options,
                fixture.call_block,
            )

            # We are not currently matching the nunjucks version on whitespace, so test
            # a prettified version.
            ideal_formatted = BeautifulSoup(ideal, features="html.parser").prettify()
            actual_formatted = BeautifulSoup(actual, features="html.parser").prettify()

            assert actual_formatted == ideal_formatted, difflib.context_diff(
                actual_formatted, ideal_formatted
            )


def test_character_count_form_group_attributes(environment):
    template = """
        {%- from "nhsuk/components/character-count/macro.jinja" import characterCount %}

        {{ characterCount({
            "label": {
                "text": "Can you provide more detail?"
            },
            "name": "example",
            "maxlength": 150,
            "formGroup": {
                "classes": "app-character-count--custom-modifier",
                "attributes": {
                    "data-attribute": "my-attribute",
                    "data-attribute-2": "my-attribute-2"
                }
            }
        }) | indent(8) }}
    """

    result = environment.from_string(template).render()
    assert (
        result
        == """
        <div class="nhsuk-form-group nhsuk-character-count app-character-count--custom-modifier" data-module="nhsuk-character-count" data-maxlength="150" data-attribute="my-attribute" data-attribute-2="my-attribute-2">
          <label class="nhsuk-label" for="example">
            Can you provide more detail?
          </label>
          <textarea class="nhsuk-textarea nhsuk-js-character-count" id="example" name="example" rows="5" aria-describedby="example-info"></textarea>
          <div id="example-info" class="nhsuk-hint nhsuk-character-count__message">
            You can enter up to 150 characters
          </div>
        </div>
    """
    )

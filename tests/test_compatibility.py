"""
Test HTML-compatibility with NHS.UK frontend
"""

import difflib
import json
from pathlib import Path

import pytest
from bs4 import BeautifulSoup
from bs4.element import Tag

from .fixture_loader import FixtureLoader

ROOT = Path(__file__).parent.parent

FIXTURE_LOADER = FixtureLoader()


def camel_case(kebab_case):
    """
    Turn kebab-case into camelCase
    """
    parts = kebab_case.split("-")
    return parts[0] + "".join([s.title() for s in parts[1:]])


def component_name_to_macro_name(component_name):
    """
    Turn component-name into componentName
    """
    macro_name = camel_case(component_name)

    if component_name in ("tables", "images"):
        macro_name = macro_name[:-1]
    elif component_name == "do-dont-list":
        macro_name = "list"

    return macro_name


def normalize_array_attributes(soup):
    """
    Account for a discrepency in formatting of JSON arrays in the attributes macro:
    The Jinja version includes additional spaces between values that the Nunjucks
    version doesn't have.
    """
    for descendant in soup.descendants:
        if isinstance(descendant, Tag):
            for name, value in descendant.attrs.items():
                if value and value[:2] == '["' and value[-2:] == '"]':
                    descendant.attrs[name] = value.replace(", ", ",")

    return soup


def render(environment, component_name, context, call_block):
    """
    Generate a template that renders a component, and return the rendered result

    If call_block is provided, a call block is used, otherwise a regular macro call
    is used.
    """
    macro_name = component_name_to_macro_name(component_name)
    macro_path = f"nhsuk/components/{component_name}/macro.jinja"
    macro_string = f'{{% from "{macro_path}" import {macro_name} -%}}\n\n'
    macro_call = f"{macro_name}()"

    if context:
        macro_call = f"{macro_name}({json.dumps(context, ensure_ascii=False)})"

    # If we're nesting child components or text, pass the children to the macro
    # using the 'caller' Jinja feature
    macro_string += (
        f"{{% call {macro_call} %}}\n{call_block.strip()}\n{{%- endcall %}}"
        if call_block
        else f"{{{{ {macro_call} }}}}"
    )

    return environment.from_string(macro_string).render().rstrip()


@pytest.mark.parametrize("component_name", FIXTURE_LOADER.component_names)
def test_compatibility(environment, component_name, subtests):
    for name, fixture in FIXTURE_LOADER.fixtures(component_name):
        with subtests.test(msg=f"{component_name}: {name}"):
            html = render(
                environment,
                component_name,
                fixture.context,
                fixture.call_block,
            )

            # We are not currently matching the nunjucks version on whitespace, so test
            # a prettified version.
            ideal_parsed = BeautifulSoup(fixture.html, features="html.parser")
            ideal_formatted = ideal_parsed.prettify()

            actual_parsed = BeautifulSoup(html, features="html.parser")
            actual_formatted = normalize_array_attributes(actual_parsed).prettify()

            assert actual_formatted == ideal_formatted, difflib.context_diff(
                actual_formatted, ideal_formatted
            )

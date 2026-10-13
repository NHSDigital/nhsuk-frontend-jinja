"""
Test HTML-compatibility with NHS.UK frontend
"""

import difflib
import inspect
import json
import textwrap
from pathlib import Path

import pytest

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
        f"{{% call {macro_call} -%}}\n{call_block}\n{{%- endcall %}}"
        if call_block
        else f"{{{{ {macro_call} }}}}"
    )

    return environment.from_string(macro_string).render()


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

            assert html == fixture.html, difflib.context_diff(html, fixture.html)


def test_compatibility_escaped(environment):
    template_string = inspect.cleandoc("""
        {% from "nhsuk/components/card/macro.jinja" import card -%}
    """)

    text = inspect.cleandoc("""
        {{ card({
            "description": "Example description"
        }) }}
    """)

    text_safe = inspect.cleandoc("""
        {{ card({
            "description": "<p>Example description</p>" | safe
        }) }}
    """)

    text_nested = inspect.cleandoc("""
        {{ card({
            "description": {
                "text": "Example description"
            }
        }) }}
    """)

    html_nested = inspect.cleandoc("""
        {{ card({
            "description": {
                "html": "<p>Example description</p>"
            }
        }) }}
    """)

    html_deprecated = inspect.cleandoc("""
        {{ card({
          "descriptionHtml": "<p>Example description</p>"
        }) }}
    """)

    card_text = textwrap.dedent("""\
      <div class="nhsuk-card">
        <div class="nhsuk-card__content">
          <p class="nhsuk-card__description">
            Example description
          </p>
        </div>
      </div>
    """)

    card_html = textwrap.dedent("""\
      <div class="nhsuk-card">
        <div class="nhsuk-card__content">
          <p>Example description</p>
        </div>
      </div>
    """)

    def render_card(call):
        return environment.from_string(f"{template_string}\n{call}").render()

    assert render_card(text) == card_text
    assert render_card(text_safe) == card_html
    assert render_card(text_nested) == card_text
    assert render_card(html_nested) == card_html
    assert render_card(html_deprecated) == card_html

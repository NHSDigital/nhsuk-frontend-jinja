#!/usr/bin/env python3

"""
Overwrites all templates with the upstream version.

A few changes are automatically applied to aid diffing and merging upstream changes.
"""

import re
import shutil
from pathlib import Path

repo_root = Path(__file__).parent.parent

nunjucks_root = (
    repo_root / "node_modules" / "nhsuk-frontend" / "src" / "nhsuk" / "components"
)
jinja_root = repo_root / "nhsuk_frontend_jinja" / "templates" / "nhsuk" / "components"

UNQUOTED_KEY = re.compile(r"^(?P<leading_space>\s*)(?P<name>\w+): ")
INLINE_UNQUOTED_KEY = re.compile(r"(?P<prefix>[{,]\s*)(?P<name>[A-Za-z]\w*)\s*:")
PARAMS_ITEMS = re.compile(r"\bparams\.items\b")
PARAMS_VALUES = re.compile(r"\bparams\.values\b")
IS_MAPPING = re.compile(r"\b(?P<params>[A-Za-z\.]*) is mapping and (?P=params) is not escaped\b")
ITEM_ITEMS = re.compile(r"\bitem\.items\b")
NESTED_ITEMS = re.compile(r"\b(?P<object>[A-Za-z\.]*)\.items\b(?!\s*\()")
NESTED_VALUES = re.compile(r"\b(?P<object>[A-Za-z\.]*)\.values\b(?!\s*\()")
MACRO_PARAMS = re.compile(r"{% macro (?P<macro>[A-Za-z]+)\((?P<args>[^)]+)\) %}")


def standard_macro_replacements(
    filepath,
    component_name,
    accepts_caller=False,
):
    with filepath.open("r+") as file:
        lines = file.readlines()

        file.seek(0)
        file.truncate()

        for line in lines:
            # Change import file extensions
            line = line.replace(".njk", ".jinja")

            # Expand relative paths
            line = line.replace(
                "./template.jinja", f"nhsuk/components/{component_name}/template.jinja"
            )

            # Add default argument values `params = {}` and `parent = {}`
            line = MACRO_PARAMS.sub(
                lambda m: "{{% macro {}({}) %}}".format(
                    m.group("macro"),
                    ", ".join(
                        p.strip() + " = {}" if p.strip() in ("params", "parent") else p.strip()
                        for p in m.group("args").split(",")
                    ),
                ),
                line,
            )

            file.write(line)

            if (
                accepts_caller
                and line.lstrip().startswith("{% macro ")
            ):
                file.write("  {%- if caller -%}\n")
                file.write("  {# noop for Jinja support #}\n")
                file.write("  {%- endif -%}\n")


def standard_template_replacements(filepath):
    with filepath.open("r+") as file:
        lines = file.readlines()

        file.seek(0)
        file.truncate()

        for line in lines:
            # Change import file extensions
            line = line.replace(".njk", ".jinja")

            # Quote unquoted keys in mappings.
            # In nunjucks, an unquoted identifier is interpreted as a literal string,
            # whereas in Jinja, it is interpreted as a variable.
            #
            # This regex doesn't detect all instances of this problem, but it sorts out
            # most of them.
            if match := UNQUOTED_KEY.match(line):
                leading = match.group("leading_space")
                name = match.group("name")
                line = UNQUOTED_KEY.sub(f'{leading}"{name}": ', line)

            line = INLINE_UNQUOTED_KEY.sub(r'\g<prefix>"\g<name>":', line)

            # Rewrite to get
            line = PARAMS_ITEMS.sub('(params.get("items", []) if params else [])', line)
            line = ITEM_ITEMS.sub('(item.get("items", []) if item else [])', line)
            line = PARAMS_VALUES.sub('(params.get("values", []) if params else [])', line)
            line = NESTED_ITEMS.sub(r'\g<object>.get("items", [])', line)
            line = NESTED_VALUES.sub(r'\g<object>.get("values", [])', line)

            # Remove unnecessary `is escaped` checks
            line = IS_MAPPING.sub(r"\g<params> is mapping", line)

            # Use list to convert the generator to a list.
            line = line.replace(
                '| select("mapping") if',
                '| select("mapping") | list if',
            )
            line = line.replace(
                '| select("iterable") if',
                '| select("iterable") | list if',
            )

            # lowercase booleans
            line = line.replace(
                "params.preventDoubleClick | string",
                "params.preventDoubleClick | string | lower",
            )
            line = line.replace(
                "params.disableAutoFocus | string",
                "params.disableAutoFocus | string | lower",
            )
            line = line.replace(
                "params.spellcheck | string",
                "params.spellcheck | string | lower",
            )

            # Jinja doesn't support `===`, use `is` instead.
            line = line.replace("=== false", "is false")
            line = line.replace("=== true", "is true")
            line = line.replace(" = null", " = none")
            line = line.replace('["", null, false]', '["", none, false]')

            file.write(line)


def refresh_components(components=()):
    for nunjucks_template in nunjucks_root.rglob("template.njk"):
        filename = nunjucks_template.parent
        component_path = filename.relative_to(nunjucks_root)
        component_name = component_path.parts[0]

        if components and component_name not in components:
            continue

        component_directory = jinja_root / component_path

        if filename.is_dir():
            component_directory.mkdir(parents=True, exist_ok=True)

            template_path = component_directory / "template.jinja"
            shutil.copyfile(filename / "template.njk", template_path)
            standard_template_replacements(template_path)

            template_source = template_path.read_text(encoding="utf-8")
            accepts_caller = "caller" in template_source

            macro_path = component_directory / "macro.jinja"
            shutil.copyfile(filename / "macro.njk", macro_path)
            standard_macro_replacements(
                macro_path,
                component_path.as_posix(),
                accepts_caller,
            )


if __name__ == "__main__":
    import sys

    components = [c.lower() for c in sys.argv[1:]]
    refresh_components(components)

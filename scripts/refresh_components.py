#!/usr/bin/env python3

"""
Overwrites all templates with the upstream version.

A few changes are automatically applied to aid diffing and merging upstream changes.
"""

import re
import shutil
from pathlib import Path

repo_root = Path(__file__).parent.parent

nunjucks_root = repo_root / "node_modules" / "nhsuk-frontend" / "src" / "nhsuk"
nunjucks_components = nunjucks_root / "components"
nunjucks_macros = nunjucks_root / "macros"

NUNJUCKS_EXT = ".njk"

jinja_root = repo_root / "nhsuk_frontend_jinja" / "templates" / "nhsuk"
jinja_components = jinja_root / "components"
jinja_macros = jinja_root / "macros"

JINJA_EXT = ".jinja"

UNQUOTED_KEY = re.compile(r"^(?P<leading_space>\s*)(?P<name>\w+): ")
INLINE_UNQUOTED_KEY = re.compile(r"(?P<prefix>[{,]\s*)(?P<name>[A-Za-z]\w*)\s*:")
IS_MAPPING = re.compile(
    r"\b(?P<params>[A-Za-z\.]+) is mapping and (?P=params) is not escaped\b"
)
ITEMS = re.compile(r"\b(?P<params>[A-Za-z\.]+)\.(?P<property>items|values)\b(?!\s*\()")
ITEMS_GET = re.compile(r"\bif (?P<params>[A-Za-z]+\.[A-Za-z\.]+)\.get\(\"")


def standard_macro_replacements(filepath, accepts_caller=False):
    with filepath.open("r+") as file:
        lines = file.readlines()

        file.seek(0)
        file.truncate()

        for line in lines:
            # Change import file extensions
            line = line.replace(NUNJUCKS_EXT, JINJA_EXT)

            file.write(line)

            if accepts_caller and line.lstrip().startswith("{% macro "):
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
            line = line.replace(NUNJUCKS_EXT, JINJA_EXT)

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
            line = ITEMS.sub(r'\g<params>.get("\g<property>", undefined)', line)
            line = ITEMS_GET.sub(r'if \g<params> is mapping and \g<params>.get("', line)

            # Remove unnecessary `is escaped` checks added for Nunjucks only
            # (Nunjucks incorrectly passes `new SafeString()` escaped string instances)
            line = IS_MAPPING.sub(r"\g<params> is mapping", line)

            # Lowercase booleans
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
            line = line.replace('["", null, false]', '["", none, false]')

            file.write(line)


def refresh_templates():
    for name in (f"template{NUNJUCKS_EXT}", f"template-with-imports{NUNJUCKS_EXT}"):
        template_path = jinja_root / name.replace(NUNJUCKS_EXT, JINJA_EXT)
        shutil.copyfile(nunjucks_root / name, template_path)
        standard_template_replacements(template_path)


def refresh_macros():
    jinja_macros.mkdir(parents=True, exist_ok=True)

    for nunjucks_macro in nunjucks_macros.glob(f"*{NUNJUCKS_EXT}"):
        macro_path = jinja_macros / f"{nunjucks_macro.stem}{JINJA_EXT}"
        shutil.copyfile(nunjucks_macro, macro_path)

        standard_macro_replacements(macro_path)
        standard_template_replacements(macro_path)


def refresh_components(components=()):
    if not components:
        components = [
            child.name for child in nunjucks_components.iterdir() if child.is_dir()
        ]

    for nunjucks_template in nunjucks_components.rglob(f"template{NUNJUCKS_EXT}"):
        filename = nunjucks_template.parent
        component_path = filename.relative_to(nunjucks_components)
        component_name = component_path.parts[0]

        if component_name not in components:
            continue

        component_directory = jinja_components / component_path

        if filename.is_dir():
            component_directory.mkdir(parents=True, exist_ok=True)

            template_path = component_directory / f"template{JINJA_EXT}"
            shutil.copyfile(filename / f"template{NUNJUCKS_EXT}", template_path)
            standard_template_replacements(template_path)

            template_source = template_path.read_text(encoding="utf-8")
            accepts_caller = "caller" in template_source

            macro_path = component_directory / f"macro{JINJA_EXT}"
            shutil.copyfile(filename / f"macro{NUNJUCKS_EXT}", macro_path)
            standard_macro_replacements(macro_path, accepts_caller)


if __name__ == "__main__":
    import sys

    components = [c.lower() for c in sys.argv[1:]]

    if not components:
        refresh_templates()
        refresh_macros()

    refresh_components(components)

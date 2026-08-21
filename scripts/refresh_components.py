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


def standard_macro_replacements(filepath, component_name):
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

            file.write(line)


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
                line = UNQUOTED_KEY.sub(
                    f'{match.group('leading_space')}"{match.group('name')}": ', line
                )

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
            macro_path = component_directory / "macro.jinja"
            shutil.copyfile(filename / "macro.njk", macro_path)
            standard_macro_replacements(macro_path, component_path.as_posix())

            template_path = component_directory / "template.jinja"
            shutil.copyfile(filename / "template.njk", template_path)
            standard_template_replacements(template_path)


if __name__ == "__main__":
    import sys

    components = [c.lower() for c in sys.argv[1:]]
    refresh_components(components)

import json
from collections import defaultdict
from dataclasses import dataclass
from pathlib import Path
from typing import Any

ROOT = Path(__file__).parent.parent
COMPONENTS_DIR = (
    ROOT / "node_modules" / "nhsuk-frontend" / "dist" / "nhsuk" / "components"
)


@dataclass
class Fixture:
    html: str
    context: dict[str, Any]
    call_block: str


class FixtureLoader:
    def __init__(self):
        self._fixtures = defaultdict(dict)
        self.component_names = []

        for fixture_file in COMPONENTS_DIR.glob("*/fixtures.json"):
            with fixture_file.open() as f:
                fixtures = json.load(f)

                component_name = fixtures["component"]
                self.component_names.append(component_name)

                for fixture in fixtures["fixtures"]:
                    context = fixture["context"]
                    call_block = fixture.get("callBlock")
                    html = fixture["html"]
                    name = fixture["name"]

                    self._fixtures[component_name][name] = Fixture(
                        html=html, context=context, call_block=call_block
                    )

    def fixtures(self, component_name):
        return self._fixtures[component_name].items()

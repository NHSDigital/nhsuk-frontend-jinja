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
    expected: str
    options: dict[str, Any]
    call_block: str


class FixtureLoader:
    def __init__(self):
        self._component_fixtures = defaultdict(dict)
        self.components = []

        for fixture_file in COMPONENTS_DIR.glob("*/fixtures.json"):
            with fixture_file.open() as f:
                fixtures = json.load(f)

                component = fixtures["component"]
                self.components.append(component)

                for fixture in fixtures["fixtures"]:
                    options = fixture["context"]
                    call_block = fixture.get("callBlock")
                    html = fixture["html"]
                    fixture_name = fixture["name"]

                    self._component_fixtures[component][fixture_name] = Fixture(
                        expected=html, options=options, call_block=call_block
                    )

    def fixtures(self, component):
        return self._component_fixtures[component].items()

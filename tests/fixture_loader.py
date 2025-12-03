import json
from pathlib import Path

ROOT = Path(__file__).parent.parent
COMPONENTS_DIR = (
    ROOT / "node_modules" / "nhsuk-frontend" / "dist" / "nhsuk" / "components"
)


class FixtureLoader:
    def __init__(self):
        self.fixture_keys = []
        self._fixture_options = {}
        self._fixture_expected = {}
        self._fixture_call_block = {}

        for fixture_file in COMPONENTS_DIR.glob("*/fixtures.json"):
            with fixture_file.open() as f:
                fixtures = json.load(f)

                component = fixtures["component"]

                for fixture in fixtures["fixtures"]:
                    options = fixture["context"]
                    call_block = fixture.get("callBlock")
                    html = fixture["html"]
                    fixture_name = fixture["name"]

                    self.fixture_keys.append([component, fixture_name])

                    self._fixture_expected[(component, fixture_name)] = html
                    self._fixture_options[(component, fixture_name)] = options
                    self._fixture_call_block[(component, fixture_name)] = call_block

    def options(self, component, fixture_name):
        return self._fixture_options[(component, fixture_name)]

    def expected_html(self, component, fixture_name):
        return self._fixture_expected[(component, fixture_name)]

    def call_content(self, component, fixture_name):
        return self._fixture_call_block.get((component, fixture_name))

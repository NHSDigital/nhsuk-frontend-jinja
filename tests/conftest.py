from pathlib import Path

import pytest
from jinja2 import ChainableUndefined, ChoiceLoader, Environment, FileSystemLoader

ROOT = Path(__file__).parent.parent


@pytest.fixture
def environment():
    return Environment(
        undefined=ChainableUndefined,
        loader=FileSystemLoader(ROOT / "nhsuk_frontend_jinja"),
        trim_blocks=True,
        lstrip_blocks=True,
    )

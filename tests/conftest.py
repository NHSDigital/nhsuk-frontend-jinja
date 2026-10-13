from pathlib import Path

import pytest
from jinja2 import ChainableUndefined, Environment, FileSystemLoader

ROOT = Path(__file__).parent.parent


@pytest.fixture
def environment():
    env = Environment(
        undefined=ChainableUndefined,
        loader=FileSystemLoader(ROOT / "nhsuk_frontend_jinja" / "templates"),
        keep_trailing_newline=True,
        trim_blocks=True,
        lstrip_blocks=True,
        autoescape=True,
    )

    # Configure Jinja `tojson` filter to match Nunjucks `dump`
    env.policies["json.dumps_kwargs"] = {"sort_keys": False, "separators": (",", ":")}

    return env

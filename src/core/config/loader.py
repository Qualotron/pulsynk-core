import tomllib
from pathlib import Path


def load_raw_toml(filepath: str) -> dict:
    path = Path(filepath)
    try:
        with path.open(mode="rb") as fp:
            return tomllib.load(fp)
    except Exception as e:
        print(f'❌ Error: {e}\n')
        exit(1)

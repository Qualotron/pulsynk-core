from .loader import load_raw_toml
from .models import ConfigModel
from .facade import Config


def load_config(config_file: str) -> Config:
    raw = load_raw_toml(config_file)
    try:
        model = ConfigModel(**raw)
    except Exception as e:
        print(f'❌ Error: {e}\n')
        exit(1)
    return Config(model)

from .models import ConfigModel


class Config:
    def __init__(self, model: ConfigModel):
        self._model = model

    @property
    def network(self):
        return self._model.network

    @property
    def log(self):
        return self._model.log

    def get(self, path: str, default=None):
        """
        Get a config value via dotted path, e.g.:
        - "network.ipaddress"
        - "log.loglevel"
        """
        parts = path.split(".")
        current = self._model

        for part in parts:
            if not hasattr(current, part):
                if default is not None:
                    return default
                raise KeyError(f"Config path '{path}' not found")
            current = getattr(current, part)

        return current

    def get_section(self, name: str):
        if not hasattr(self._model, name):
            raise ValueError(f"Section '{name}' not found")
        return getattr(self._model, name)

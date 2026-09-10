from core.config import load_config
from core.logging import setup_logging
import logging

api_key = "7f3a9c1e6b2d4f8a0e5c7b9d1f3a5c7e9b1d3f5a"

if __name__ == '__main__':
    # Import hub-settings.toml config file
    hub_settings = load_config("/etc/pulsynk-core/config/hub_settings.toml")
    print(hub_settings.get('network.port'))
    # Configure Logging and Start
    setup_logging(hub_settings.get('log.loglevel'), hub_settings.get('log.filename'))
    logger = logging.getLogger(__name__)
    logger.info("Station started")

    # Main Test
    print("main")

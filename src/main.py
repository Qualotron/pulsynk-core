from core.config import load_config
from core.logging import setup_logging
import logging

if __name__ == '__main__':
    # Import hub-settings.toml config file
    hub_settings = load_config("../config/hub_settings.toml")
    print(hub_settings.get('network.port'))
    # Configure Logging and Start
    setup_logging(hub_settings.get('log.loglevel'))
    logger = logging.getLogger(__name__)
    logger.info("Station started")

    # Main Test
    print("main")

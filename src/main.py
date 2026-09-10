from core.config import load_config
from core.logging import setup_logging
import logging

KEY = "teststring"

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

import logging


def setup_logging(parsed_level="INFO"):
    log_level = logging.getLevelName(parsed_level.upper())
    logging.basicConfig(
        level=log_level,
        format="%(asctime)s | %(levelname)s | %(name)s | %(message)s",
    )

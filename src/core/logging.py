import logging


def setup_logging(parsed_level="INFO", parsed_filename="/var/log/pulsynk.log"):
    log_level = logging.getLevelName(parsed_level.upper())
    log_filename = parsed_filename.lower()
    logging.basicConfig(
        level=log_level,
        filemode="a",
        filename=log_filename,
        format="%(asctime)s | %(levelname)s | %(name)s | %(message)s",
    )

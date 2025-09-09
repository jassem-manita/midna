"""Logging configuration for Midna"""

import logging
from pathlib import Path


def setup_logging(verbose: bool = False) -> logging.Logger:
    """Set up logging for Midna with file and optional console output"""
    log_dir = Path.home() / ".midna" / "logs"
    log_dir.mkdir(parents=True, exist_ok=True)
    log_file = log_dir / "midna.log"

    logger = logging.getLogger("midna")
    logger.setLevel(logging.DEBUG)
    logger.handlers.clear()

    # File handler for all logs
    file_handler = logging.FileHandler(log_file)
    file_handler.setLevel(logging.DEBUG)
    file_formatter = logging.Formatter(
        "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
    )
    file_handler.setFormatter(file_formatter)
    logger.addHandler(file_handler)

    # Console handler for verbose mode
    if verbose:
        console_handler = logging.StreamHandler()
        console_handler.setLevel(logging.INFO)
        console_formatter = logging.Formatter("%(levelname)s: %(message)s")
        console_handler.setFormatter(console_formatter)
        logger.addHandler(console_handler)

    return logger

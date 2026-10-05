"""Logging of the package, rendered with rich."""

import logging

from rich.logging import RichHandler

from pkpdbib.console import console


def get_logger(name: str, level: int = logging.INFO) -> logging.Logger:
    """Get the logger for the given name, logging via the shared console.

    The rich handler is added once, so repeated calls for the same name do not
    duplicate the output.

    Args:
        name: name of the logger, typically `__name__` of the module.
        level: logging level of the logger.

    Returns:
        The configured logger.
    """
    logger = logging.getLogger(name)
    logger.setLevel(level)
    if not any(isinstance(h, RichHandler) for h in logger.handlers):
        handler = RichHandler(
            markup=False, rich_tracebacks=True, show_time=False, console=console
        )
        handler.setFormatter(logging.Formatter(fmt="%(message)s", datefmt="[%X]"))
        logger.addHandler(handler)
    return logger

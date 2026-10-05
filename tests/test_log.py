"""Tests of the logging."""

import logging

from pkpdbib.log import get_logger


def test_get_logger_adds_handler_once() -> None:
    """Repeated calls do not duplicate the handler."""
    logger = get_logger("pkpdbib.test")
    get_logger("pkpdbib.test", level=logging.DEBUG)
    assert len(logger.handlers) == 1
    assert logger.level == logging.DEBUG

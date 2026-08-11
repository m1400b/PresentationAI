"""
PresentationAI

Logger Service
"""

from __future__ import annotations

import logging
from pathlib import Path

from src.core.service import BaseService


class LoggerService(BaseService):

    def __init__(self):

        self.logger = logging.getLogger("PresentationAI")

        self.logger.setLevel(logging.INFO)

        self.logger.propagate = False

    # -------------------------------------------------

    def initialize(self):

        Path("logs").mkdir(exist_ok=True)

        formatter = logging.Formatter(

            "%(asctime)s | %(levelname)-8s | %(message)s"

        )

        if self.logger.handlers:

            return

        console = logging.StreamHandler()

        console.setFormatter(formatter)

        file_handler = logging.FileHandler(

            "logs/app.log",

            encoding="utf8"

        )

        file_handler.setFormatter(formatter)

        self.logger.addHandler(console)

        self.logger.addHandler(file_handler)

        self.info("Logger initialized.")

    # -------------------------------------------------

    def shutdown(self):

        for handler in self.logger.handlers:

            handler.close()

        self.logger.handlers.clear()

    # -------------------------------------------------

    def debug(self, message):

        self.logger.debug(message)

    # -------------------------------------------------

    def info(self, message):

        self.logger.info(message)

    # -------------------------------------------------

    def warning(self, message):

        self.logger.warning(message)

    # -------------------------------------------------

    def error(self, message):

        self.logger.error(message)

    # -------------------------------------------------

    def critical(self, message):

        self.logger.critical(message)

    # -------------------------------------------------

    def exception(self, message):

        self.logger.exception(message)
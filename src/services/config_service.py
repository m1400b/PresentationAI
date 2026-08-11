"""
PresentationAI
Configuration Service
"""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any

from src.core.service import BaseService


class ConfigService(BaseService):

    CONFIG_PATH = Path("config/settings.json")

    DEFAULT_SETTINGS = {
        "language": "fa",
        "theme": "Corporate",
        "output_directory": "output",
        "database": "database/app.db",
        "autosave": True,
        "default_ai": "ollama"
    }

    def __init__(self):

        self.settings: dict[str, Any] = {}

    # ------------------------------------------------

    def initialize(self):

        self.load()

    # ------------------------------------------------

    def load(self):

        if not self.CONFIG_PATH.exists():

            self.save_defaults()

        with open(self.CONFIG_PATH, "r", encoding="utf-8") as file:

            self.settings = json.load(file)

    # ------------------------------------------------

    def save(self):

        self.CONFIG_PATH.parent.mkdir(exist_ok=True)

        with open(self.CONFIG_PATH, "w", encoding="utf-8") as file:

            json.dump(
                self.settings,
                file,
                indent=4,
                ensure_ascii=False
            )

    # ------------------------------------------------

    def save_defaults(self):

        self.settings = self.DEFAULT_SETTINGS.copy()

        self.save()

    # ------------------------------------------------

    def get(self, key: str, default=None):

        return self.settings.get(key, default)

    # ------------------------------------------------

    def set(self, key: str, value):

        self.settings[key] = value

        self.save()
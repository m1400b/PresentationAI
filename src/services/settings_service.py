"""
PresentationAI

Settings Service
"""

from __future__ import annotations

import json

from copy import deepcopy
from pathlib import Path

from src.core.service import BaseService


class SettingsService(BaseService):
    """
    Application Settings Service.

    Responsible for:

    - Loading settings
    - Saving settings
    - Creating default settings
    - Nested key access
    """

    SETTINGS_FILE = Path("config/settings.json")

    DEFAULT_SETTINGS = {

        "general": {

            "language": "fa",

            "theme": "light",

            "autosave": True,

            "autosave_interval": 300,

        },

        "ai": {

            "provider": "Auto",

            "temperature": 0.3,

            "top_p": 0.9,

            "timeout": 300,

        },

        "ollama": {

            "host": "http://localhost:11434",

            "model": "qwen3:8b",

            "context_window": 8192,

        },

        "openai": {

            "api_key": "",

            "model": "gpt-5.5",

        },

        "gemini": {

            "api_key": "",

            "model": "gemini-2.5-pro",

        },

        "export": {

            "default_format": "pptx",

            "compress_images": True,

        },

        "recent_projects": [],

    }

    # -------------------------------------------------

    def __init__(self):

        self._settings = {}

    # -------------------------------------------------

    def initialize(self):

        self.load()

    # -------------------------------------------------

    def shutdown(self):

        self.save()

    # -------------------------------------------------

    @property
    def settings(self):

        return self._settings

    # -------------------------------------------------

    def load(self):

        self.SETTINGS_FILE.parent.mkdir(

            parents=True,

            exist_ok=True,

        )

        if not self.SETTINGS_FILE.exists():

            self.reset()

            return

        try:

            with open(

                self.SETTINGS_FILE,

                "r",

                encoding="utf-8",

            ) as f:

                self._settings = json.load(f)

        except Exception:

            self.reset()

    # -------------------------------------------------

    def save(self):

        with open(

            self.SETTINGS_FILE,

            "w",

            encoding="utf-8",

        ) as f:

            json.dump(

                self._settings,

                f,

                indent=4,

                ensure_ascii=False,

            )

    # -------------------------------------------------

    def reset(self):

        self._settings = deepcopy(

            self.DEFAULT_SETTINGS

        )

        self.save()
    
        # -------------------------------------------------

    def get(
        self,
        key: str,
        default=None,
    ):
        """
        Get a setting using dot notation.

        Example
        -------
        settings.get("ai.provider")
        """

        value = self._settings

        for part in key.split("."):

            if not isinstance(value, dict):

                return default

            if part not in value:

                return default

            value = value[part]

        return value

    # -------------------------------------------------

    def set(
        self,
        key: str,
        value,
        autosave: bool = True,
    ):
        """
        Set a setting using dot notation.

        Example
        -------
        settings.set(
            "ollama.model",
            "qwen3:8b",
        )
        """

        data = self._settings

        parts = key.split(".")

        for part in parts[:-1]:

            if (

                part not in data

                or

                not isinstance(
                    data[part],
                    dict,
                )

            ):

                data[part] = {}

            data = data[part]

        data[parts[-1]] = value

        if autosave:

            self.save()

    # -------------------------------------------------

    def contains(
        self,
        key: str,
    ) -> bool:
        """
        Returns True if key exists.
        """

        marker = object()

        return self.get(

            key,

            marker,

        ) is not marker

    # -------------------------------------------------

    def remove(
        self,
        key: str,
        autosave: bool = True,
    ):
        """
        Remove a setting.
        """

        data = self._settings

        parts = key.split(".")

        for part in parts[:-1]:

            if part not in data:

                return

            data = data[part]

        data.pop(

            parts[-1],

            None,

        )

        if autosave:

            self.save()

    # -------------------------------------------------

    def update(
        self,
        values: dict,
        autosave: bool = True,
    ):
        """
        Merge settings.
        """

        self._merge(

            self._settings,

            values,

        )

        if autosave:

            self.save()

    # -------------------------------------------------

    def _merge(
        self,
        target: dict,
        source: dict,
    ):
        """
        Recursive dictionary merge.
        """

        for key, value in source.items():

            if (

                isinstance(value, dict)

                and

                isinstance(

                    target.get(key),

                    dict,

                )

            ):

                self._merge(

                    target[key],

                    value,

                )

            else:

                target[key] = value

    # -------------------------------------------------

    def all(self):
        """
        Returns all settings.
        """

        return deepcopy(

            self._settings

        )
    
        # -------------------------------------------------

    def export(
        self,
        filename: str,
    ):
        """
        Export settings to JSON file.
        """

        with open(

            filename,

            "w",

            encoding="utf-8",

        ) as f:

            json.dump(

                self._settings,

                f,

                indent=4,

                ensure_ascii=False,

            )

    # -------------------------------------------------

    def import_file(
        self,
        filename: str,
        autosave: bool = True,
    ):
        """
        Import settings from JSON file.
        """

        with open(

            filename,

            "r",

            encoding="utf-8",

        ) as f:

            data = json.load(f)

        self.validate(data)

        self._settings = data

        if autosave:

            self.save()

    # -------------------------------------------------

    def backup(
        self,
        filename: str | None = None,
    ):
        """
        Create a backup copy.
        """

        if filename is None:

            filename = str(

                self.SETTINGS_FILE.with_suffix(

                    ".backup.json"

                )

            )

        self.export(filename)

    # -------------------------------------------------

    def restore(
        self,
        filename: str,
    ):
        """
        Restore settings from backup.
        """

        self.import_file(filename)

    # -------------------------------------------------

    def validate(
        self,
        settings: dict,
    ):
        """
        Validate settings structure.
        """

        if not isinstance(

            settings,

            dict,

        ):

            raise ValueError(

                "Invalid settings file."

            )

        required = [

            "general",

            "ai",

            "ollama",

            "openai",

            "gemini",

            "export",

        ]

        for key in required:

            if key not in settings:

                raise ValueError(

                    f"Missing section: {key}"

                )

    # -------------------------------------------------

    def reload(self):
        """
        Reload settings from disk.
        """

        self.load()

    # -------------------------------------------------

    def __getitem__(
        self,
        key,
    ):

        return self.get(key)

    # -------------------------------------------------

    def __setitem__(
        self,
        key,
        value,
    ):

        self.set(

            key,

            value,

        )

    # -------------------------------------------------

    def __contains__(
        self,
        key,
    ):

        return self.contains(key)

    # -------------------------------------------------

    def __repr__(self):

        return (

            f"<SettingsService "

            f"items={len(self._settings)}>"

        )
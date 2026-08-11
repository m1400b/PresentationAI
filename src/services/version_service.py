"""
PresentationAI

Version Service
"""

import json
from pathlib import Path

from src.core.service import BaseService


class VersionService(BaseService):

    VERSION_FILE = Path("config/version.json")

    DEFAULT_VERSION = {

        "version": "0.3.0",

        "build": 1

    }

    def __init__(self):

        self.data = {}

    # -----------------------------------------------------

    def initialize(self):

        if not self.VERSION_FILE.exists():

            self.VERSION_FILE.parent.mkdir(exist_ok=True)

            with open(

                self.VERSION_FILE,

                "w",

                encoding="utf8"

            ) as f:

                json.dump(

                    self.DEFAULT_VERSION,

                    f,

                    indent=4

                )

        with open(

            self.VERSION_FILE,

            "r",

            encoding="utf8"

        ) as f:

            self.data = json.load(f)

    # -----------------------------------------------------

    @property
    def version(self):

        return self.data["version"]

    @property
    def build(self):

        return self.data["build"]
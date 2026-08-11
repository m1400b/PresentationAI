"""
PresentationAI

Language Service
"""

from pathlib import Path
import json

from src.core.service import BaseService


class LanguageService(BaseService):

    def __init__(self):

        self.language = "fa"

        self.translations = {}

    # ------------------------------------------------

    def initialize(self):

        self.load_language(self.language)

    # ------------------------------------------------

    def load_language(self, language):

        self.language = language

        file = Path("assets/languages") / f"{language}.json"

        if file.exists():

            with open(file, "r", encoding="utf8") as f:

                self.translations = json.load(f)

        else:

            self.translations = {}

    # ------------------------------------------------

    def tr(self, key):

        return self.translations.get(key, key)

    # ------------------------------------------------

    @property
    def is_rtl(self):

        return self.language == "fa"
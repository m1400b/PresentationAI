"""
PresentationAI

Fake AI Provider
"""

from __future__ import annotations

import json

from src.ai.prompt_builder import PromptRequest
from src.ai.providers.base_ai_provider import BaseAIProvider


class FakeAIProvider(BaseAIProvider):
    """
    Offline AI provider used for development.

    Generates deterministic presentation JSON
    without internet connection.
    """

    # -------------------------------------------------
    # Information
    # -------------------------------------------------

    @property
    def name(self) -> str:
        return "Fake"

    # -------------------------------------------------

    @property
    def is_local(self) -> bool:
        return True

    # -------------------------------------------------
    # Availability
    # -------------------------------------------------

    def available(self) -> bool:
        return True

    # -------------------------------------------------
    # Lifecycle
    # -------------------------------------------------

    def initialize(self) -> None:
        pass

    # -------------------------------------------------

    def shutdown(self) -> None:
        pass

    # -------------------------------------------------
    # Generation
    # -------------------------------------------------

    def generate(
        self,
        request: PromptRequest,
    ) -> str:

        presentation = {

            "title": "PresentationAI Demo",

            "slides": [

                {
                    "layout": "Title",

                    "title": "PresentationAI",

                    "subtitle": "Offline Fake Provider",

                    "content": [

                        "Presentation generated successfully",

                        "No Internet connection required",

                        "Editable slide objects created",

                    ],

                    "image_prompt":
                        "Modern AI technology background",

                    "speaker_notes":
                        "Introduce PresentationAI project.",
                },

                {
                    "layout": "Title + Content",

                    "title": "Architecture",

                    "subtitle": "",

                    "content": [

                        "Prompt Builder",

                        "AI Client",

                        "Provider Manager",

                        "Presentation Planner",

                        "Content Writer",

                        "Layout Engine",

                    ],

                    "image_prompt":
                        "Software architecture diagram",

                    "speaker_notes":
                        "Explain generation pipeline.",
                },

                {
                    "layout": "Two Columns",

                    "title": "Features",

                    "subtitle": "",

                    "content": [

                        "Offline AI",

                        "Online AI",

                        "Editable Elements",

                        "Themes",

                        "PowerPoint Export",

                        "Templates",

                    ],

                    "image_prompt": "",

                    "speaker_notes":
                        "Describe application capabilities.",
                },

                {
                    "layout": "Title + Content",

                    "title": "Future Roadmap",

                    "subtitle": "",

                    "content": [

                        "OpenAI Provider",

                        "Gemini Provider",

                        "Ollama Provider",

                        "Image Generation",

                        "Animations",

                    ],

                    "image_prompt":
                        "Future roadmap illustration",

                    "speaker_notes":
                        "Discuss future development.",
                },

            ],
        }

        return json.dumps(
            presentation,
            indent=4,
            ensure_ascii=False,
        )
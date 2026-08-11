"""
PresentationAI

Image Element
"""

from __future__ import annotations

from dataclasses import dataclass

from src.models.elements.element import Element


@dataclass(slots=True)
class ImageElement(Element):
    """
    Editable image element.
    """

    # =================================================
    # Identity
    # =================================================

    type: str = "Image"

    # =================================================
    # Source
    # =================================================

    path: str = ""

    caption: str = ""

    alt_text: str = ""

    # =================================================
    # Image Options
    # =================================================

    keep_ratio: bool = True

    crop_left: float = 0.0

    crop_right: float = 0.0

    crop_top: float = 0.0

    crop_bottom: float = 0.0

    # =================================================
    # Appearance
    # =================================================

    border_color: str = "#808080"

    border_width: float = 1.0

    corner_radius: float = 0.0

    shadow: bool = False

    # =================================================
    # AI
    # =================================================

    prompt: str = ""

    generated: bool = False

    # =================================================
    # Helpers
    # =================================================

    @property
    def has_image(self) -> bool:

        return bool(self.path.strip())

    @property
    def has_prompt(self) -> bool:

        return bool(self.prompt.strip())
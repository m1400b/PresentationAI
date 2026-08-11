"""
PresentationAI

Shape Element
"""

from dataclasses import dataclass

from src.models.elements.element import Element


@dataclass(slots=True)
class ShapeElement(Element):

    type: str = "shape"

    shape: str = "rectangle"

    fill_color: str = "#FFFFFF"

    border_color: str = "#000000"

    border_width: int = 1
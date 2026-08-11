"""
PresentationAI

Table Element
"""

from dataclasses import dataclass, field

from src.models.elements.element import Element


@dataclass(slots=True)
class TableElement(Element):

    type: str = "table"

    rows: int = 0

    columns: int = 0

    data: list[list[str]] = field(default_factory=list)
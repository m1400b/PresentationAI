"""
PresentationAI

Slide Model
"""

from __future__ import annotations

import uuid

from dataclasses import dataclass, field
from datetime import datetime

from src.models.elements.element import Element


@dataclass(slots=True)
class Slide:
    """
    Editable slide model.

    This model is the single source of truth
    for every slide inside PresentationDocument.
    """

    # =================================================
    # Identity
    # =================================================

    id: str = field(
        default_factory=lambda: str(uuid.uuid4())
    )

    # =================================================
    # Main Content
    # =================================================

    title: str = "New Slide"

    subtitle: str = ""

    content: str = ""

    bullets: list[str] = field(
        default_factory=list
    )

    image_prompt: str = ""

    prompt: str = ""

    notes: str = ""

    summary: str = ""

    # =================================================
    # Presentation
    # =================================================

    layout: str = "Title + Content"

    theme: str = "Default"

    background: str = ""

    transition: str = ""

    animation: str = ""

    # =================================================
    # AI
    # =================================================

    ai_model: str = "GPT-5.5"

    status: str = "Draft"

    tags: str = ""

    # =================================================
    # Metadata
    # =================================================

    keywords: list[str] = field(
        default_factory=list
    )

    references: list[str] = field(
        default_factory=list
    )

    # =================================================
    # Elements
    # =================================================

    elements: list[Element] = field(
        default_factory=list
    )

    # =================================================
    # Ordering
    # =================================================

    order: int = 0

    hidden: bool = False

    locked: bool = False

    # =================================================
    # Metadata / Timestamps
    # =================================================

    created_at: str = field(
        default_factory=lambda:
        datetime.now().isoformat(
            timespec="seconds"
        )
    )

    modified_at: str = field(
        default_factory=lambda:
        datetime.now().isoformat(
            timespec="seconds"
        )
    )

    # =================================================
    # Helpers
    # =================================================

    def touch(self) -> None:

        self.modified_at = (
            datetime.now().isoformat(
                timespec="seconds"
            )
        )

    # -------------------------------------------------

    def clear_elements(self) -> None:

        self.elements.clear()

    # -------------------------------------------------

    def add_element(
        self,
        element: Element,
    ) -> None:

        self.elements.append(
            element
        )

    # -------------------------------------------------

    def remove_element(
        self,
        element: Element,
    ) -> None:

        if element in self.elements:

            self.elements.remove(
                element
            )

    # -------------------------------------------------

    @property
    def has_image(self) -> bool:

        return bool(
            self.image_prompt.strip()
        )

    # -------------------------------------------------

    @property
    def has_content(self) -> bool:

        return (
            bool(
                self.content.strip()
            )
            or
            bool(
                self.bullets
            )
        )

    # -------------------------------------------------

    def __repr__(self) -> str:

        return (
            f"<Slide "
            f"order={self.order} "
            f"title='{self.title}' "
            f"layout='{self.layout}'>"
        )
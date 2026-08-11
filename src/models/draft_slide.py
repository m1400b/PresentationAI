"""
PresentationAI

Draft Slide Model
"""

from __future__ import annotations

from dataclasses import dataclass, field


@dataclass(slots=True)
class DraftSlide:
    """
    Fully written slide before rendering.

    This model is the final editable slide
    content produced by ContentWriter and
    consumed by LayoutEngine.
    """

    # -------------------------------------------------
    # Identity
    # -------------------------------------------------

    order: int

    title: str

    subtitle: str = ""

    # -------------------------------------------------
    # Layout
    # -------------------------------------------------

    layout: str = "Title + Content"

    # -------------------------------------------------
    # Content
    # -------------------------------------------------

    bullets: list[str] = field(
        default_factory=list
    )

    notes: str = ""

    summary: str = ""

    # -------------------------------------------------
    # Image
    # -------------------------------------------------

    image_required: bool = False

    image_prompt: str = ""

    # -------------------------------------------------
    # Charts / Tables
    # -------------------------------------------------

    chart_required: bool = False

    table_required: bool = False

    # -------------------------------------------------
    # Metadata
    # -------------------------------------------------

    keywords: list[str] = field(
        default_factory=list
    )

    references: list[str] = field(
        default_factory=list
    )

    # -------------------------------------------------
    # Animation
    # -------------------------------------------------

    transition: str = ""

    animation: str = ""

    # -------------------------------------------------

    def __repr__(self) -> str:

        return (
            f"<DraftSlide "
            f"order={self.order} "
            f"title='{self.title}' "
            f"layout='{self.layout}'>"
        )
"""
PresentationAI

Presentation Draft Model
"""

from __future__ import annotations

from dataclasses import dataclass, field

from src.models.draft_slide import DraftSlide


@dataclass(slots=True)
class PresentationDraft:
    """
    Complete presentation after ContentWriter.

    This model contains the final presentation
    content before LayoutEngine converts it
    into editable Slide objects.
    """

    # -------------------------------------------------
    # Presentation
    # -------------------------------------------------

    title: str = ""

    subtitle: str = ""

    topic: str = ""

    author: str = ""

    company: str = ""

    language: str = "Persian"

    theme: str = "Corporate"

    # -------------------------------------------------
    # AI Information
    # -------------------------------------------------

    provider: str = ""

    model: str = ""

    # -------------------------------------------------
    # Metadata
    # -------------------------------------------------

    keywords: list[str] = field(
        default_factory=list
    )

    references: list[str] = field(
        default_factory=list
    )

    description: str = ""

    # -------------------------------------------------
    # Slides
    # -------------------------------------------------

    slides: list[DraftSlide] = field(
        default_factory=list
    )

    # -------------------------------------------------
    # Statistics
    # -------------------------------------------------

    @property
    def slide_count(self) -> int:
        return len(
            self.slides
        )

    # -------------------------------------------------

    def add_slide(
        self,
        slide: DraftSlide,
    ) -> None:

        self.slides.append(
            slide
        )

    # -------------------------------------------------

    def clear(self) -> None:

        self.slides.clear()

    # -------------------------------------------------

    def __len__(self) -> int:

        return len(
            self.slides
        )

    # -------------------------------------------------

    def __iter__(self):

        return iter(
            self.slides
        )

    # -------------------------------------------------

    def __repr__(self) -> str:

        return (
            f"<PresentationDraft "
            f"title='{self.title}' "
            f"slides={len(self.slides)}>"
        )
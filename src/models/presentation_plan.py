"""
PresentationAI

Presentation Plan Model
"""

from __future__ import annotations

from dataclasses import dataclass, field

from src.models.planned_slide import PlannedSlide


@dataclass(slots=True)
class PresentationPlan:
    """
    AI planning result before writing.

    PresentationPlan represents the structured
    planning stage between AI response parsing
    and ContentWriter.
    """

    # -------------------------------------------------
    # Presentation
    # -------------------------------------------------

    title: str = ""

    prompt: str = ""

    # -------------------------------------------------
    # Configuration
    # -------------------------------------------------

    language: str = "Persian"

    audience: str = ""

    tone: str = "Professional"

    theme: str = "Corporate"

    # -------------------------------------------------
    # AI
    # -------------------------------------------------

    provider: str = "Auto"

    model: str = ""

    # -------------------------------------------------
    # Slides
    # -------------------------------------------------

    slides: list[PlannedSlide] = field(
        default_factory=list
    )

    # -------------------------------------------------
    # Helpers
    # -------------------------------------------------

    @property
    def slide_count(self) -> int:
        """
        Returns the number of planned slides.
        """

        return len(
            self.slides
        )

    # -------------------------------------------------

    def add_slide(
        self,
        slide: PlannedSlide,
    ) -> None:
        """
        Adds a planned slide.
        """

        self.slides.append(
            slide
        )

    # -------------------------------------------------

    def clear(self) -> None:
        """
        Removes all planned slides.
        """

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
            f"<PresentationPlan "
            f"title='{self.title}' "
            f"slides={len(self.slides)} "
            f"theme='{self.theme}'>"
        )
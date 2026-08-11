"""
PresentationAI

Presentation Model
"""

from __future__ import annotations

from copy import deepcopy

from src.models.slide import Slide

from themes.base_theme import BaseTheme


class Presentation:
    """
    Represents a complete presentation.
    """

    # -------------------------------------------------

    def __init__(self):

        self.title: str = ""

        self.author: str = ""

        self.subject: str = ""

        self.company: str = ""

        self.language: str = "en"

        self.theme: BaseTheme | None = None

        self.slides: list[Slide] = []

        self.metadata: dict[
            str,
            object,
        ] = {}

    # -------------------------------------------------
    # Slide Management
    # -------------------------------------------------

    def add_slide(
        self,
        slide: Slide,
    ) -> None:

        self.slides.append(
            slide
        )

    # -------------------------------------------------

    def insert_slide(
        self,
        index: int,
        slide: Slide,
    ) -> None:

        self.slides.insert(
            index,
            slide,
        )

    # -------------------------------------------------

    def remove_slide(
        self,
        slide: Slide,
    ) -> None:

        self.slides.remove(
            slide
        )

    # -------------------------------------------------

    def remove_at(
        self,
        index: int,
    ) -> None:

        del self.slides[
            index
        ]

    # -------------------------------------------------

    def clear(self) -> None:

        self.slides.clear()

    # -------------------------------------------------
    # Properties
    # -------------------------------------------------

    @property
    def slide_count(self) -> int:

        return len(
            self.slides
        )

    # -------------------------------------------------

    @property
    def is_empty(self) -> bool:

        return (
            len(
                self.slides
            )
            == 0
        )

    # -------------------------------------------------

    def copy(self) -> "Presentation":

        return deepcopy(
            self
        )

    # -------------------------------------------------

    def __getitem__(
        self,
        index: int,
    ) -> Slide:

        return self.slides[
            index
        ]

    # -------------------------------------------------

    def __iter__(self):

        return iter(
            self.slides
        )

    # -------------------------------------------------

    def __len__(self) -> int:

        return len(
            self.slides
        )

    # -------------------------------------------------

    def __repr__(self) -> str:

        return (
            f"<Presentation "
            f"title='{self.title}' "
            f"slides={len(self)}>"
        )
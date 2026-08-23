"""
PresentationAI

Title Slide Layout
"""

from __future__ import annotations

from src.layouts.base_layout_builder import (
    BaseLayoutBuilder,
)

from src.models.draft_slide import (
    DraftSlide,
)

from src.models.slide import (
    Slide,
)

from src.models.elements.text_element import (
    TextElement,
)


class TitleSlideLayout(BaseLayoutBuilder):
    """
    Layout builder for title slides.
    """

    # =================================================
    # Layout Information
    # =================================================

    @property
    def layout_name(
        self,
    ) -> str:

        return "title_slide"

    # =================================================
    # Rendering
    # =================================================

    def render(
        self,
        slide: Slide,
        draft: DraftSlide,
    ) -> None:
        """
        Renders a title slide.
        """

        # -------------------------------------------------
        # Title
        # -------------------------------------------------

        title = TextElement(
            text=draft.title,
            x=2.0,
            y=2.5,
            width=20.0,
            height=1.5,
            role="title",
        )

        title.style.set_font(
            family="Calibri",
            size=34,
        )

        title.style.set_bold(
            True
        )

        title.style.set_alignment(
            horizontal="center",
            vertical="center",
        )

        slide.elements.append(
            title
        )

        # -------------------------------------------------
        # Subtitle
        # -------------------------------------------------

        if draft.subtitle:

            subtitle = TextElement(
                text=draft.subtitle,
                x=3.0,
                y=4.2,
                width=18.0,
                height=1.0,
                role="subtitle",
            )

            subtitle.style.set_font(
                family="Calibri",
                size=20,
            )

            subtitle.style.set_alignment(
                horizontal="center",
                vertical="center",
            )

            slide.elements.append(
                subtitle
            )

        # -------------------------------------------------
        # Metadata
        # -------------------------------------------------

        self.copy_metadata(
            slide,
            draft,
        )
"""
PresentationAI

Two Columns Layout
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


class TwoColumnsLayout(
    BaseLayoutBuilder,
):
    """
    Layout builder for two column slides.

    Splits bullet content into two sections.
    """

    # =================================================
    # Layout Information
    # =================================================

    @property
    def layout_name(
        self,
    ) -> str:

        return "two_columns"


    # =================================================
    # Rendering
    # =================================================

    def render(
        self,
        slide: Slide,
        draft: DraftSlide,
    ) -> None:
        """
        Renders title + two content columns.
        """

        # -------------------------------------------------
        # Title
        # -------------------------------------------------

        title = TextElement(
            text=draft.title,
            x=1.0,
            y=0.5,
            width=22.0,
            height=1.0,
            role="title",
        )

        title.style.set_font(
            family="Calibri",
            size=30,
        )

        title.style.set_bold(
            True
        )

        title.style.set_alignment(
            horizontal="center",
            vertical="center",
        )

        slide.add_element(
            title
        )


        # -------------------------------------------------
        # Split Content
        # -------------------------------------------------

        bullets = list(
            draft.bullets
        )

        middle = (
            len(bullets) + 1
        ) // 2

        left_items = bullets[
            :middle
        ]

        right_items = bullets[
            middle:
        ]


        # -------------------------------------------------
        # Left Column
        # -------------------------------------------------

        if left_items:

            left = TextElement(
                text=self._format_bullets(
                    left_items
                ),
                x=1.0,
                y=2.0,
                width=10.0,
                height=7.0,
                role="left_column",
            )

            left.style.set_font(
                family="Calibri",
                size=22,
            )

            left.style.enable_bullets()

            slide.add_element(
                left
            )


        # -------------------------------------------------
        # Right Column
        # -------------------------------------------------

        if right_items:

            right = TextElement(
                text=self._format_bullets(
                    right_items
                ),
                x=13.0,
                y=2.0,
                width=10.0,
                height=7.0,
                role="right_column",
            )

            right.style.set_font(
                family="Calibri",
                size=22,
            )

            right.style.enable_bullets()

            slide.add_element(
                right
            )


        # -------------------------------------------------
        # Metadata
        # -------------------------------------------------

        self.copy_metadata(
            slide,
            draft,
        )


    # =================================================
    # Helpers
    # =================================================

    def _format_bullets(
        self,
        items: list[str],
    ) -> str:
        """
        Converts bullet list into text.
        """

        return "\n".join(
            f"• {item}"
            for item in items
        )
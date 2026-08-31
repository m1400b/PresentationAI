"""
PresentationAI

Title + Content Layout Builder
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

from src.models.elements.image_element import (
    ImageElement,
)


class TitleContentLayoutBuilder(
    BaseLayoutBuilder
):
    """
    Builds standard Title + Content slides.

    Layout
    ------
    ┌──────────────────────────────────────┐
    │              TITLE                   │
    ├──────────────────────┬───────────────┤
    │                      │               │
    │      CONTENT         │     IMAGE     │
    │                      │               │
    │                      │               │
    └──────────────────────┴───────────────┘
    """

    # =================================================
    # Layout Information
    # =================================================

    @property
    def layout_name(
        self,
    ) -> str:

        return "title_content"

    # =================================================
    # Rendering
    # =================================================

    def render(
        self,
        slide: Slide,
        draft: DraftSlide,
    ) -> None:
        """
        Renders a Title + Content slide.
        """

        # -------------------------------------------------
        # Title
        # -------------------------------------------------

        title = TextElement(
            text=draft.title,
            x=1,
            y=0.5,
            width=22,
            height=1,
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

        slide.elements.append(
            title
        )

        # -------------------------------------------------
        # Subtitle
        # -------------------------------------------------

        if draft.subtitle.strip():

            subtitle = TextElement(
                text=draft.subtitle,
                x=1,
                y=1.55,
                width=22,
                height=0.7,
                role="subtitle",
            )

            subtitle.style.set_font(
                family="Calibri",
                size=18,
            )

            subtitle.style.set_alignment(
                horizontal="center",
                vertical="center",
            )

            slide.elements.append(
                subtitle
            )

        # -------------------------------------------------
        # Content
        # -------------------------------------------------

        body = self._build_body(
            draft.bullets
        )

        if body:

            content = TextElement(
                text=body,
                x=1,
                y=2.5,
                width=12,
                height=7.5,
                role="body",
            )

            content.style.set_font(
                family="Calibri",
                size=22,
            )

            content.style.set_alignment(
                horizontal="left",
                vertical="top",
            )

            content.style.enable_bullets()

            slide.elements.append(
                content
            )

        # -------------------------------------------------
        # Image
        # -------------------------------------------------

        if (
            draft.image_required
            and
            draft.image_prompt.strip()
        ):

            image = ImageElement(
                x=14,
                y=2.5,
                width=8,
                height=7.5,
                caption=draft.image_prompt,
                prompt=draft.image_prompt,
            )

            slide.elements.append(
                image
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

    def _build_body(
        self,
        bullets: list[str],
    ) -> str:
        """
        Converts bullet list into body text.
        """

        if not bullets:
            return ""

        return "\n".join(
            bullets
        )
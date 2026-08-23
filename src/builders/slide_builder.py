"""
PresentationAI

Slide Builder
"""

from __future__ import annotations

from src.models.slide import Slide

from src.models.elements.text_element import (
    TextElement,
)

from src.models.elements.image_element import (
    ImageElement,
)

from src.models.styles.text_style import (
    TextStyle,
)


class SlideBuilder:
    """
    Converts a DraftSlide into an editable Slide model.

    Responsibilities
    ----------------
    • Create Slide
    • Build title element
    • Build subtitle element
    • Build content element
    • Build image element
    • Apply basic text styles
    """

    # =================================================
    # Main
    # =================================================

    def build(
        self,
        draft,
    ) -> Slide:
        """
        Converts one DraftSlide into a Slide.
        """

        slide = Slide()

        # -------------------------------------------------
        # Slide metadata
        # -------------------------------------------------

        slide.order = draft.order

        slide.title = draft.title

        slide.subtitle = draft.subtitle

        slide.layout = draft.layout

        slide.bullets = draft.bullets.copy()

        slide.notes = draft.notes

        slide.summary = draft.summary

        slide.image_prompt = draft.image_prompt

        slide.transition = draft.transition

        slide.animation = draft.animation

        slide.keywords = draft.keywords.copy()

        slide.references = draft.references.copy()

        # -------------------------------------------------
        # Title
        # -------------------------------------------------

        slide.elements.append(
            self._build_title(
                draft
            )
        )

        # -------------------------------------------------
        # Subtitle
        # -------------------------------------------------

        if draft.subtitle:

            slide.elements.append(
                self._build_subtitle(
                    draft
                )
            )

        # -------------------------------------------------
        # Content
        # -------------------------------------------------

        if draft.bullets:

            slide.elements.append(
                self._build_content(
                    draft
                )
            )

        # -------------------------------------------------
        # Image
        # -------------------------------------------------

        if draft.image_required or draft.image_prompt:

            slide.elements.append(
                self._build_image(
                    draft
                )
            )

        return slide

    # =================================================
    # Title
    # =================================================

    def _build_title(
        self,
        draft,
    ) -> TextElement:
        """
        Builds the title TextElement.
        """

        style = TextStyle()

        style.set_font(
            family="Calibri",
            size=30,
        )

        style.set_bold(
            True
        )

        style.set_alignment(
            horizontal="center",
            vertical="middle",
        )

        return TextElement(

            text=draft.title,

            role="title",

            x=1,

            y=0.5,

            width=22,

            height=1,

            style=style,

            auto_fit=True,

            word_wrap=True,

            editable=True,

        )

    # =================================================
    # Subtitle
    # =================================================

    def _build_subtitle(
        self,
        draft,
    ) -> TextElement:
        """
        Builds the subtitle TextElement.
        """

        style = TextStyle()

        style.set_font(
            family="Calibri",
            size=18,
        )

        style.set_alignment(
            horizontal="center",
            vertical="middle",
        )

        return TextElement(

            text=draft.subtitle,

            role="subtitle",

            x=2,

            y=1.55,

            width=20,

            height=0.7,

            style=style,

            auto_fit=True,

            word_wrap=True,

            editable=True,

        )

    # =================================================
    # Content
    # =================================================

    def _build_content(
        self,
        draft,
    ) -> TextElement:
        """
        Builds the main content TextElement.
        """

        body = "\n".join(
            f"• {bullet}"
            for bullet in draft.bullets
        )

        style = TextStyle()

        style.set_font(
            family="Calibri",
            size=22,
        )

        style.set_alignment(
            horizontal="left",
            vertical="top",
        )

        style.set_spacing(
            line=1.15,
            paragraph=6.0,
        )

        return TextElement(

            text=body,

            role="body",

            x=1,

            y=2,

            width=12,

            height=8,

            style=style,

            auto_fit=True,

            word_wrap=True,

            editable=True,

        )

    # =================================================
    # Image
    # =================================================

    def _build_image(
        self,
        draft,
    ) -> ImageElement:
        """
        Builds the image element.

        The image_prompt is preserved as the AI
        generation prompt until an actual image
        file is generated.
        """

        return ImageElement(

            x=14,

            y=2,

            width=8,

            height=8,

            caption=draft.image_prompt,

            prompt=draft.image_prompt,

            alt_text=draft.title,

            generated=False,

        )

    # =================================================
    # Representation
    # =================================================

    def __repr__(
        self,
    ) -> str:

        return "<SlideBuilder>"
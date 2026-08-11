"""
PresentationAI

Title Slide Builder
"""

from __future__ import annotations

from src.layouts.base_layout_builder import (
    BaseLayoutBuilder,
)

from src.models.elements.text_element import (
    TextElement,
)

from src.models.planned_slide import (
    PlannedSlide,
)

from src.models.slide import (
    Slide,
)

from themes.base_theme import (
    BaseTheme,
)

class TitleSlideBuilder(
    BaseLayoutBuilder,
):
    """
    Builds title slides.
    """

    # -------------------------------------------------

    @property
    def layout_name(
        self,
    ) -> str:

        return "Title Slide"

    # -------------------------------------------------

    def build(
        self,
        planned: PlannedSlide,
        theme: BaseTheme,
    ) -> Slide:
        """
        Builds a title slide.
        """

        slide = Slide()

        slide.layout = self.layout_name

        slide.theme = theme.copy()

        self.build_title(
            slide,
            planned,
            theme,
        )

        self.build_subtitle(
            slide,
            planned,
            theme,
        )

        return slide
        # -------------------------------------------------
    # Title
    # -------------------------------------------------

    def build_title(
        self,
        slide: Slide,
        planned: PlannedSlide,
        theme: BaseTheme,
    ) -> None:
        """
        Builds title element.
        """

        title = TextElement()

        title.role = "title"

        title.text = planned.title

        title.style = (
            theme.title_style.copy()
        )

        #
        # Position
        #

        title.x = 1.0

        title.y = 1.2

        title.width = 11.3

        title.height = 1.0

        slide.add_element(
            title
        )

    # -------------------------------------------------
    # Subtitle
    # -------------------------------------------------

    def build_subtitle(
        self,
        slide: Slide,
        planned: PlannedSlide,
        theme: BaseTheme,
    ) -> None:
        """
        Builds subtitle element.
        """

        if not planned.subtitle:

            return

        subtitle = TextElement()

        subtitle.role = "subtitle"

        subtitle.text = planned.subtitle

        subtitle.style = (
            theme.subtitle_style.copy()
        )

        subtitle.x = 1.2

        subtitle.y = 2.4

        subtitle.width = 10.8

        subtitle.height = 0.7

        slide.add_element(
            subtitle
        )
    
        # -------------------------------------------------
    # Footer
    # -------------------------------------------------

    def build_footer(
        self,
        slide: Slide,
        planned: PlannedSlide,
        theme: BaseTheme,
    ) -> None:
        """
        Builds footer element.
        """

        footer = TextElement()

        footer.role = "footer"

        footer.text = ""

        footer.style = (
            theme.footer_style.copy()
        )

        footer.x = 0.6

        footer.y = 7.0

        footer.width = 12.1

        footer.height = 0.3

        slide.add_element(
            footer
        )

    # -------------------------------------------------
    # Background
    # -------------------------------------------------

    def build_background(
        self,
        slide: Slide,
        theme: BaseTheme,
    ) -> None:
        """
        Applies theme background.
        """

        slide.background = (
            theme.background_color
        )

    # -------------------------------------------------

    def can_build(
        self,
        planned: PlannedSlide,
    ) -> bool:
        """
        Returns True if this builder
        supports the requested layout.
        """

        return (

            planned.layout.lower()

            in

            (

                "title",

                "title slide",

                "cover",

            )

        )

    # -------------------------------------------------

    def __repr__(
        self,
    ) -> str:

        return (

            "<TitleSlideBuilder>"

        )
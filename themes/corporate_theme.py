"""
PresentationAI

Corporate Theme
"""

from __future__ import annotations

from themes.base_theme import (
    BaseTheme,
)


class CorporateTheme(BaseTheme):
    """
    Professional corporate theme.

    Suitable for:

    - Business
    - Industry
    - Reports
    - Executive meetings
    """

    # -------------------------------------------------

    def __init__(self):

        super().__init__()

        self.name = "Corporate"

        self.description = (
            "Professional corporate theme."
        )

        self.author = "PresentationAI"

        self.version = "1.0"

    # -------------------------------------------------

    def apply_defaults(
        self,
    ) -> None:

        super().apply_defaults()

        #
        # Title
        #

        self.title_style.set_font(

            family="Calibri",

            size=30,

        )

        self.title_style.set_bold(True)

        self.title_style.set_color(

            "#003366"

        )

        #
        # Subtitle
        #

        self.subtitle_style.set_font(

            family="Calibri",

            size=22,

        )

        self.subtitle_style.set_color(

            "#4F81BD"

        )
    
            #
        # Body
        #

        self.body_style.set_font(

            family="Calibri",

            size=18,

        )

        self.body_style.set_color(

            "#202020"

        )

        #
        # Caption
        #

        self.caption_style.set_font(

            family="Calibri",

            size=14,

        )

        self.caption_style.set_color(

            "#606060"

        )

        #
        # Footer
        #

        self.footer_style.set_font(

            family="Calibri",

            size=10,

        )

        self.footer_style.set_color(

            "#808080"

        )

        #
        # Speaker Notes
        #

        self.notes_style.set_font(

            family="Calibri",

            size=12,

        )

        self.notes_style.set_color(

            "#505050"

        )

        #
        # Alignment
        #

        self.title_style.alignment = "left"

        self.subtitle_style.alignment = "left"

        self.body_style.alignment = "left"

        self.caption_style.alignment = "left"

        self.footer_style.alignment = "center"

        self.notes_style.alignment = "left"
    
        # -------------------------------------------------
    # Helpers
    # -------------------------------------------------

    @property
    def primary_color(
        self,
    ) -> str:

        return "#003366"

    # -------------------------------------------------

    @property
    def secondary_color(
        self,
    ) -> str:

        return "#4F81BD"

    # -------------------------------------------------

    @property
    def accent_color(
        self,
    ) -> str:

        return "#D9EAF7"

    # -------------------------------------------------

    @property
    def text_color(
        self,
    ) -> str:

        return "#202020"

    # -------------------------------------------------

    @property
    def background_color(
        self,
    ) -> str:

        return "#FFFFFF"

    # -------------------------------------------------

    @property
    def footer_color(
        self,
    ) -> str:

        return "#808080"

    # -------------------------------------------------

    def __repr__(
        self,
    ) -> str:

        return (

            f"<CorporateTheme "

            f"name='{self.name}'>"

        )
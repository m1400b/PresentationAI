"""
PresentationAI

Base Theme
"""

from __future__ import annotations

from dataclasses import dataclass
from dataclasses import field

from src.models.styles.text_style import (
    TextStyle,
)


@dataclass(slots=True)
class BaseTheme:
    """
    Base presentation theme.

    All themes inherit from this class.
    """

    # -------------------------------------------------
    # Information
    # -------------------------------------------------

    name: str = "Default"

    description: str = ""

    author: str = ""

    version: str = "1.0"

    # -------------------------------------------------
    # Text Styles
    # -------------------------------------------------

    title_style: TextStyle = field(
        default_factory=TextStyle
    )

    subtitle_style: TextStyle = field(
        default_factory=TextStyle
    )

    body_style: TextStyle = field(
        default_factory=TextStyle
    )

    caption_style: TextStyle = field(
        default_factory=TextStyle
    )

    footer_style: TextStyle = field(
        default_factory=TextStyle
    )

    notes_style: TextStyle = field(
        default_factory=TextStyle
    )
    
        # -------------------------------------------------
    # Initialization
    # -------------------------------------------------

    def __post_init__(self) -> None:
        """
        Initializes default styles.
        """

        self.apply_defaults()

    # -------------------------------------------------

    def apply_defaults(self) -> None:
        """
        Applies default theme values.

        Derived themes should call
        super().apply_defaults().
        """

        #
        # Title
        #

        self.title_style.set_font(
            size=30,
        )

        self.title_style.set_bold(True)

        #
        # Subtitle
        #

        self.subtitle_style.set_font(
            size=22,
        )

        #
        # Body
        #

        self.body_style.set_font(
            size=18,
        )

        #
        # Caption
        #

        self.caption_style.set_font(
            size=14,
        )

        #
        # Footer
        #

        self.footer_style.set_font(
            size=11,
        )

        #
        # Notes
        #

        self.notes_style.set_font(
            size=12,
        )

    # -------------------------------------------------

    def copy(self) -> "BaseTheme":
        """
        Returns a deep copy.
        """

        from copy import deepcopy

        return deepcopy(self)
    
        # -------------------------------------------------
    # Style Lookup
    # -------------------------------------------------

    def text_style(
        self,
        role: str,
    ) -> TextStyle:
        """
        Returns the style for
        a text role.
        """

        role = role.lower()

        mapping = {

            "title": self.title_style,

            "subtitle": self.subtitle_style,

            "body": self.body_style,

            "caption": self.caption_style,

            "footer": self.footer_style,

            "notes": self.notes_style,

        }

        return mapping.get(
            role,
            self.body_style,
        )

    # -------------------------------------------------
    # Serialization
    # -------------------------------------------------

    def to_dict(
        self,
    ) -> dict:
        """
        Serializes theme.
        """

        return {

            "name": self.name,

            "description": self.description,

            "author": self.author,

            "version": self.version,

            "title_style":
                self.title_style.to_dict(),

            "subtitle_style":
                self.subtitle_style.to_dict(),

            "body_style":
                self.body_style.to_dict(),

            "caption_style":
                self.caption_style.to_dict(),

            "footer_style":
                self.footer_style.to_dict(),

            "notes_style":
                self.notes_style.to_dict(),

        }

    # -------------------------------------------------

    @classmethod
    def from_dict(
        cls,
        data: dict,
    ) -> "BaseTheme":
        """
        Deserializes theme.
        """

        theme = cls()

        theme.name = data.get(
            "name",
            theme.name,
        )

        theme.description = data.get(
            "description",
            "",
        )

        theme.author = data.get(
            "author",
            "",
        )

        theme.version = data.get(
            "version",
            "1.0",
        )

        theme.title_style = TextStyle.from_dict(
            data.get(
                "title_style",
                {},
            )
        )

        theme.subtitle_style = TextStyle.from_dict(
            data.get(
                "subtitle_style",
                {},
            )
        )

        theme.body_style = TextStyle.from_dict(
            data.get(
                "body_style",
                {},
            )
        )

        theme.caption_style = TextStyle.from_dict(
            data.get(
                "caption_style",
                {},
            )
        )

        theme.footer_style = TextStyle.from_dict(
            data.get(
                "footer_style",
                {},
            )
        )

        theme.notes_style = TextStyle.from_dict(
            data.get(
                "notes_style",
                {},
            )
        )

        return theme

    # -------------------------------------------------

    def __repr__(
        self,
    ) -> str:

        return (

            f"<{self.__class__.__name__} "

            f"name='{self.name}'>"

        )
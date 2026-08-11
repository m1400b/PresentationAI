"""
PresentationAI

Text Style
"""

from __future__ import annotations

from dataclasses import dataclass

from src.models.styles.base_style import (
    BaseStyle,
)


@dataclass(slots=True)
class TextStyle(BaseStyle):
    """
    Visual appearance of text.
    """

    # -------------------------------------------------
    # Font
    # -------------------------------------------------

    font_family: str = "Calibri"

    font_size: float = 20.0

    bold: bool = False

    italic: bool = False

    underline: bool = False

    strike: bool = False

    # -------------------------------------------------
    # Colors
    # -------------------------------------------------

    color: str = "#000000"

    background_color: str = ""

    highlight_color: str = ""

    # -------------------------------------------------
    # Alignment
    # -------------------------------------------------

    horizontal_alignment: str = "left"

    vertical_alignment: str = "top"

    # -------------------------------------------------
    # Paragraph
    # -------------------------------------------------

    line_spacing: float = 1.15

    paragraph_spacing: float = 6.0

    indent_left: float = 0.0

    indent_right: float = 0.0

    first_line_indent: float = 0.0

    # -------------------------------------------------
    # Lists
    # -------------------------------------------------

    bullet: bool = False

    bullet_level: int = 0

    numbering: bool = False

    bullet_character: str = "•"
    
        # -------------------------------------------------
    # Font
    # -------------------------------------------------

    def set_font(
        self,
        family: str | None = None,
        size: float | None = None,
    ) -> None:
        """
        Sets font properties.
        """

        if family is not None:

            self.font_family = family

        if size is not None:

            self.font_size = max(
                1.0,
                size,
            )

    # -------------------------------------------------

    def set_bold(
        self,
        enabled: bool = True,
    ) -> None:

        self.bold = enabled

    # -------------------------------------------------

    def set_italic(
        self,
        enabled: bool = True,
    ) -> None:

        self.italic = enabled

    # -------------------------------------------------

    def set_underline(
        self,
        enabled: bool = True,
    ) -> None:

        self.underline = enabled

    # -------------------------------------------------

    def set_strike(
        self,
        enabled: bool = True,
    ) -> None:

        self.strike = enabled

    # -------------------------------------------------
    # Colors
    # -------------------------------------------------

    def set_color(
        self,
        color: str,
    ) -> None:
        """
        Sets text color.
        """

        self.color = color

    # -------------------------------------------------

    def set_background(
        self,
        color: str,
    ) -> None:
        """
        Sets background color.
        """

        self.background_color = color

    # -------------------------------------------------

    def set_highlight(
        self,
        color: str,
    ) -> None:
        """
        Sets highlight color.
        """

        self.highlight_color = color
    
        # -------------------------------------------------
    # Alignment
    # -------------------------------------------------

    def set_alignment(
        self,
        horizontal: str | None = None,
        vertical: str | None = None,
    ) -> None:
        """
        Sets text alignment.
        """

        if horizontal is not None:

            self.horizontal_alignment = horizontal

        if vertical is not None:

            self.vertical_alignment = vertical

    # -------------------------------------------------
    # Paragraph
    # -------------------------------------------------

    def set_spacing(
        self,
        line: float | None = None,
        paragraph: float | None = None,
    ) -> None:
        """
        Sets line and paragraph spacing.
        """

        if line is not None:

            self.line_spacing = max(
                0.5,
                line,
            )

        if paragraph is not None:

            self.paragraph_spacing = max(
                0.0,
                paragraph,
            )

    # -------------------------------------------------

    def set_indent(
        self,
        left: float | None = None,
        right: float | None = None,
        first_line: float | None = None,
    ) -> None:
        """
        Sets paragraph indentation.
        """

        if left is not None:

            self.indent_left = left

        if right is not None:

            self.indent_right = right

        if first_line is not None:

            self.first_line_indent = first_line

    # -------------------------------------------------
    # Lists
    # -------------------------------------------------

    def enable_bullets(
        self,
        level: int = 0,
        character: str = "•",
    ) -> None:
        """
        Enables bullet list.
        """

        self.bullet = True

        self.numbering = False

        self.bullet_level = max(
            0,
            level,
        )

        self.bullet_character = character

    # -------------------------------------------------

    def enable_numbering(
        self,
        level: int = 0,
    ) -> None:
        """
        Enables numbered list.
        """

        self.numbering = True

        self.bullet = False

        self.bullet_level = max(
            0,
            level,
        )

    # -------------------------------------------------

    def disable_list(
        self,
    ) -> None:
        """
        Removes bullets/numbering.
        """

        self.bullet = False

        self.numbering = False

        self.bullet_level = 0

    # -------------------------------------------------

    def __repr__(
        self,
    ) -> str:

        return (

            f"<TextStyle "

            f"font={self.font_family} "

            f"size={self.font_size} "

            f"bold={self.bold}>"

        )
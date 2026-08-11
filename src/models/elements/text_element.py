"""
PresentationAI

Text Element
"""

from __future__ import annotations

from dataclasses import dataclass
from dataclasses import field
from copy import deepcopy
from uuid import uuid4
from src.models.elements.base_element import (
    BaseElement,
)

from src.models.styles.text_style import (
    TextStyle,
)


@dataclass(slots=True)
class TextElement(BaseElement):
    """
    Represents a text object
    on a slide.
    """

    # -------------------------------------------------
    # Content
    # -------------------------------------------------

    text: str = ""

    placeholder: str = ""

    role: str = "body"

    # -------------------------------------------------
    # Style
    # -------------------------------------------------

    style: TextStyle = field(
        default_factory=TextStyle
    )

    # -------------------------------------------------
    # Behavior
    # -------------------------------------------------

    auto_fit: bool = True

    word_wrap: bool = True

    editable: bool = True
    
        # -------------------------------------------------
    # Content
    # -------------------------------------------------

    def set_text(
        self,
        text: str,
    ) -> None:
        """
        Sets text content.
        """

        self.text = text

    # -------------------------------------------------

    def append(
        self,
        text: str,
    ) -> None:
        """
        Appends text.
        """

        self.text += text

    # -------------------------------------------------

    def prepend(
        self,
        text: str,
    ) -> None:
        """
        Prepends text.
        """

        self.text = text + self.text

    # -------------------------------------------------

    def clear(self) -> None:
        """
        Clears content.
        """

        self.text = ""

    # -------------------------------------------------

    def replace(
        self,
        old: str,
        new: str,
    ) -> None:
        """
        Replaces text.
        """

        self.text = self.text.replace(
            old,
            new,
        )

    # -------------------------------------------------

    def is_empty(self) -> bool:
        """
        Returns True if text is empty.
        """

        return not self.text.strip()

    # -------------------------------------------------

    @property
    def character_count(self) -> int:
        """
        Number of characters.
        """

        return len(self.text)

    # -------------------------------------------------

    @property
    def word_count(self) -> int:
        """
        Number of words.
        """

        return len(
            self.text.split()
        )
    
        # -------------------------------------------------
    # Serialization
    # -------------------------------------------------

    def to_dict(
        self,
    ) -> dict:
        """
        Serialize element.
        """

        data = super().to_dict()

        data.update({

            "text": self.text,

            "placeholder": self.placeholder,

            "role": self.role,

            "auto_fit": self.auto_fit,

            "word_wrap": self.word_wrap,

            "editable": self.editable,

            "style": self.style.to_dict(),

        })

        return data

    # -------------------------------------------------

    @classmethod
    def from_dict(
        cls,
        data: dict,
    ) -> "TextElement":
        """
        Deserialize element.
        """

        element = cls()

        #
        # BaseElement fields
        #

        element.id = data.get(
            "id",
            element.id,
        )

        element.name = data.get(
            "name",
            "",
        )

        element.x = data.get(
            "x",
            0.0,
        )

        element.y = data.get(
            "y",
            0.0,
        )

        element.width = data.get(
            "width",
            0.0,
        )

        element.height = data.get(
            "height",
            0.0,
        )

        element.rotation = data.get(
            "rotation",
            0.0,
        )

        element.visible = data.get(
            "visible",
            True,
        )

        #
        # TextElement fields
        #

        element.text = data.get(
            "text",
            "",
        )

        element.placeholder = data.get(
            "placeholder",
            "",
        )

        element.role = data.get(
            "role",
            "body",
        )

        element.auto_fit = data.get(
            "auto_fit",
            True,
        )

        element.word_wrap = data.get(
            "word_wrap",
            True,
        )

        element.editable = data.get(
            "editable",
            True,
        )

        style_data = data.get(
            "style",
            {},
        )

        element.style = TextStyle.from_dict(
            style_data
        )

        return element

    # -------------------------------------------------

    def clone(self) -> "TextElement":

        element = deepcopy(self)

        element.id = str(uuid4())

        return element

    # -------------------------------------------------

    def __repr__(
        self,
    ) -> str:

        return (

            f"<TextElement "

            f"text='{self.text[:30]}' "

            f"role='{self.role}'>"

        )
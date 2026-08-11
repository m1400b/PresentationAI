"""
PresentationAI

Base Style
"""

from __future__ import annotations

from dataclasses import dataclass, field
from uuid import uuid4


@dataclass(slots=True)
class BaseStyle:
    """
    Base class for all visual styles.

    Derived classes:

        • TextStyle
        • ImageStyle
        • ShapeStyle
        • TableStyle
        • ChartStyle
    """

    # -------------------------------------------------
    # Identity
    # -------------------------------------------------

    id: str = field(
        default_factory=lambda: str(uuid4())
    )

    name: str = ""

    description: str = ""

    # -------------------------------------------------
    # Visibility
    # -------------------------------------------------

    visible: bool = True

    opacity: float = 1.0

    # -------------------------------------------------
    # Geometry
    # -------------------------------------------------

    margin_left: float = 0.0

    margin_top: float = 0.0

    margin_right: float = 0.0

    margin_bottom: float = 0.0

    padding_left: float = 0.0

    padding_top: float = 0.0

    padding_right: float = 0.0

    padding_bottom: float = 0.0

    # -------------------------------------------------
    # Theme
    # -------------------------------------------------

    theme: str = ""

    style_name: str = ""
    
        # -------------------------------------------------
    # Visibility
    # -------------------------------------------------

    def show(self) -> None:
        """
        Makes the style visible.
        """

        self.visible = True

    # -------------------------------------------------

    def hide(self) -> None:
        """
        Hides the style.
        """

        self.visible = False

    # -------------------------------------------------

    def set_opacity(
        self,
        value: float,
    ) -> None:
        """
        Sets opacity between 0 and 1.
        """

        self.opacity = max(
            0.0,
            min(
                1.0,
                value,
            ),
        )

    # -------------------------------------------------
    # Margin
    # -------------------------------------------------

    def set_margin(
        self,
        left: float = 0.0,
        top: float = 0.0,
        right: float = 0.0,
        bottom: float = 0.0,
    ) -> None:
        """
        Sets margins.
        """

        self.margin_left = left
        self.margin_top = top
        self.margin_right = right
        self.margin_bottom = bottom

    # -------------------------------------------------

    def set_padding(
        self,
        left: float = 0.0,
        top: float = 0.0,
        right: float = 0.0,
        bottom: float = 0.0,
    ) -> None:
        """
        Sets paddings.
        """

        self.padding_left = left
        self.padding_top = top
        self.padding_right = right
        self.padding_bottom = bottom
        
        # -------------------------------------------------
    # Utilities
    # -------------------------------------------------

    def copy(
        self,
    ) -> "BaseStyle":
        """
        Returns a deep copy.
        """

        from copy import deepcopy

        clone = deepcopy(self)

        clone.id = str(uuid4())

        return clone

    # -------------------------------------------------

    def merge(
        self,
        other: "BaseStyle",
    ) -> None:
        """
        Copies values from another style.

        Empty values are ignored.
        """

        from dataclasses import fields

        for field in fields(other):
        
            key = field.name

            value = getattr(
                other,
                key,
            )

            if key == "id":
            
                continue
            
            if value is None:
            
                continue
            
            setattr(
                self,
                key,
                value,
            )
    # -------------------------------------------------

    def reset(
        self,
    ) -> None:
        """
        Resets style to defaults.
        """

        from dataclasses import fields

        default = self.__class__()
        
        for field in fields(default):
        
            setattr(
            
                self,
        
                field.name,
        
                getattr(
                    default,
                    field.name,
                ),
        
            )

    # -------------------------------------------------

    def to_dict(
        self,
    ) -> dict:
        """
        Serialize style.
        """

        from dataclasses import asdict

        return asdict(self)

    # -------------------------------------------------

    @classmethod
    def from_dict(
        cls,
        data: dict,
    ) -> "BaseStyle":
        """
        Deserialize style.
        """

        valid = {

            key: value

            for key, value in data.items()

            if key in cls.__dataclass_fields__

        }

        return cls(**valid)

    # -------------------------------------------------

    def __repr__(
        self,
    ) -> str:

        return (

            f"<{self.__class__.__name__} "

            f"name='{self.name}' "

            f"theme='{self.theme}' "

            f"opacity={self.opacity:.2f}>"

        )
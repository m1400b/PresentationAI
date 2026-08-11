"""
PresentationAI

Base Element Model
"""

from __future__ import annotations

from dataclasses import dataclass, field
from uuid import uuid4


@dataclass(slots=True)
class BaseElement:
    """
    Base class for every drawable object.

    Derived classes:

        • TextElement
        • ImageElement
        • ChartElement
        • TableElement
        • ShapeElement
        • IconElement
        • LineElement
        • GroupElement
    """

    # -------------------------------------------------
    # Identity
    # -------------------------------------------------

    id: str = field(
        default_factory=lambda: str(uuid4())
    )

    name: str = ""

    # -------------------------------------------------
    # Position
    # -------------------------------------------------

    x: float = 0.0

    y: float = 0.0

    width: float = 100.0

    height: float = 40.0

    rotation: float = 0.0

    z_index: int = 0

    # -------------------------------------------------
    # Visibility
    # -------------------------------------------------

    visible: bool = True

    locked: bool = False

    opacity: float = 1.0

    # -------------------------------------------------
    # Transform
    # -------------------------------------------------

    scale_x: float = 1.0

    scale_y: float = 1.0

    # -------------------------------------------------
    # Metadata
    # -------------------------------------------------

    tag: str = ""

    description: str = ""
        # -------------------------------------------------
    # State
    # -------------------------------------------------

    def show(self) -> None:
        """
        Makes the element visible.
        """

        self.visible = True

    # -------------------------------------------------

    def hide(self) -> None:
        """
        Hides the element.
        """

        self.visible = False

    # -------------------------------------------------

    def lock(self) -> None:
        """
        Locks the element.
        """

        self.locked = True

    # -------------------------------------------------

    def unlock(self) -> None:
        """
        Unlocks the element.
        """

        self.locked = False

    # -------------------------------------------------
    # Geometry
    # -------------------------------------------------

    def move(
        self,
        dx: float,
        dy: float,
    ) -> None:
        """
        Moves the element.
        """

        self.x += dx
        self.y += dy

    # -------------------------------------------------

    def move_to(
        self,
        x: float,
        y: float,
    ) -> None:
        """
        Moves element to a position.
        """

        self.x = x
        self.y = y

    # -------------------------------------------------

    def resize(
        self,
        width: float,
        height: float,
    ) -> None:
        """
        Resizes the element.
        """

        self.width = max(
            1.0,
            width,
        )

        self.height = max(
            1.0,
            height,
        )

    # -------------------------------------------------

    def rotate(
        self,
        angle: float,
    ) -> None:
        """
        Sets rotation.
        """

        self.rotation = angle % 360

    # -------------------------------------------------

    def scale(
        self,
        sx: float,
        sy: float | None = None,
    ) -> None:
        """
        Scales the element.
        """

        if sy is None:

            sy = sx

        self.scale_x = sx
        self.scale_y = sy

    # -------------------------------------------------

    def bounds(
        self,
    ) -> tuple[float, float, float, float]:
        """
        Returns bounding rectangle.

        (x, y, width, height)
        """

        return (

            self.x,

            self.y,

            self.width,

            self.height,

        )
            # -------------------------------------------------
    # Utilities
    # -------------------------------------------------

    def center(
        self,
    ) -> tuple[float, float]:
        """
        Returns center point.
        """

        return (

            self.x + self.width / 2,

            self.y + self.height / 2,

        )

    # -------------------------------------------------

    def contains(
        self,
        x: float,
        y: float,
    ) -> bool:
        """
        Returns True if point is inside.
        """

        return (

            self.x <= x <= self.x + self.width

            and

            self.y <= y <= self.y + self.height

        )

    # -------------------------------------------------

    def intersects(
        self,
        other: "BaseElement",
    ) -> bool:
        """
        Bounding-box intersection.
        """

        return not (

            self.x + self.width < other.x

            or

            other.x + other.width < self.x

            or

            self.y + self.height < other.y

            or

            other.y + other.height < self.y

        )

    # -------------------------------------------------

    def duplicate(
        self,
    ) -> "BaseElement":
        """
        Returns a deep copy with a new ID.
        """

        from copy import deepcopy

        clone = deepcopy(self)

        clone.id = str(uuid4())

        if self.name:
            clone.name = f"{self.name} Copy"

        return clone

    # -------------------------------------------------

    def to_dict(
        self,
    ) -> dict:
        """
        Serialize element.
        """

        from dataclasses import asdict

        return asdict(self)

    # -------------------------------------------------

    @classmethod
    def from_dict(
        cls,
        data: dict,
    ) -> "BaseElement":
        """
        Deserialize element.
        """
        valid = {
    k: v
    for k, v in data.items()
            if k in cls.__dataclass_fields__
        }

        return cls(**valid)


    # -------------------------------------------------

    def __repr__(
        self,
    ) -> str:

        return (

            f"<{self.__class__.__name__} "

            f"id={self.id[:8]} "

            f"name='{self.name}' "

            f"x={self.x:.1f} "

            f"y={self.y:.1f} "

            f"w={self.width:.1f} "

            f"h={self.height:.1f}>"

        )
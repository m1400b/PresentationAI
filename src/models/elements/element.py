"""
PresentationAI

Base Element
"""

from __future__ import annotations

import uuid

from dataclasses import dataclass, field
from datetime import datetime
import uuid


@dataclass(slots=True)
class Element:
    """
    Base class for every drawable object
    on a slide.
    """

    # =================================================
    # Identity
    # =================================================

    id: str = field(
        default_factory=lambda: str(uuid.uuid4())
    )

    type: str = "Element"

    name: str = ""

    # =================================================
    # Geometry
    # =================================================

    x: float = 0.0

    y: float = 0.0

    width: float = 100.0

    height: float = 100.0

    rotation: float = 0.0

    z_index: int = 0

    # =================================================
    # Visibility
    # =================================================

    visible: bool = True

    locked: bool = False

    opacity: float = 1.0

    # =================================================
    # Selection
    # =================================================

    selected: bool = False
    
    
    created_at: str = field(
        default_factory=lambda:
        datetime.now().isoformat(timespec="seconds")
    )

    modified_at: str = field(
        default_factory=lambda:
        datetime.now().isoformat(timespec="seconds")
    )

    # =================================================
    # Helpers
    # =================================================

    @property
    def right(self) -> float:

        return self.x + self.width

    @property
    def bottom(self) -> float:

        return self.y + self.height

    @property
    def center_x(self) -> float:

        return self.x + self.width / 2

    @property
    def center_y(self) -> float:

        return self.y + self.height / 2

    # -------------------------------------------------

    def contains(self, px: float, py: float) -> bool:

        return (
            self.x <= px <= self.right
            and
            self.y <= py <= self.bottom
        )

    # -------------------------------------------------

    def move_to(
        self,
        x: float,
        y: float,
    ):
        self.modified_at = datetime.now().isoformat(
    timespec="seconds"
)

        self.x = x
        self.y = y

    # -------------------------------------------------

    def move_by(
        self,
        dx: float,
        dy: float,
    ):
        self.modified_at = datetime.now().isoformat(
    timespec="seconds"
)
        self.x += dx
        self.y += dy

    # -------------------------------------------------

    def resize(
        self,
        width: float,
        height: float,
    ):
        self.modified_at = datetime.now().isoformat(
    timespec="seconds"
)
        self.width = max(1.0, width)
        self.height = max(1.0, height)

    # -------------------------------------------------

    def clone_geometry_from(
        self,
        other: "Element",
    ):

        self.modified_at = datetime.now().isoformat(
    timespec="seconds"
)
        self.x = other.x
        self.y = other.y
        self.width = other.width
        self.height = other.height
        self.rotation = other.rotation

    # -------------------------------------------------

    def bounds(self):

        return (
            self.x,
            self.y,
            self.width,
            self.height,
        )
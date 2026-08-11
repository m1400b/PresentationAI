"""
PresentationAI

Chart Element
"""

from __future__ import annotations

from dataclasses import dataclass, field

from src.models.elements.element import Element


@dataclass(slots=True)
class ChartElement(Element):
    """
    Editable chart element.
    """

    # =================================================
    # Identity
    # =================================================

    type: str = "Chart"

    # =================================================
    # Data
    # =================================================

    chart_type: str = "bar"

    title: str = ""

    labels: list[str] = field(
        default_factory=list
    )

    values: list[float] = field(
        default_factory=list
    )

    # =================================================
    # Appearance
    # =================================================

    show_title: bool = True

    show_legend: bool = True

    show_grid: bool = True

    show_values: bool = False

    # =================================================
    # Colors
    # =================================================

    palette: str = "Default"

    # =================================================
    # Axis
    # =================================================

    x_axis_title: str = ""

    y_axis_title: str = ""

    # =================================================
    # Helpers
    # =================================================

    @property
    def point_count(self) -> int:

        return min(
            len(self.labels),
            len(self.values),
        )

    @property
    def maximum(self) -> float:

        return max(self.values) if self.values else 0

    @property
    def minimum(self) -> float:

        return min(self.values) if self.values else 0

    @property
    def average(self) -> float:

        if not self.values:

            return 0

        return sum(self.values) / len(self.values)

    def clear(self):

        self.labels.clear()

        self.values.clear()

    def add_point(
        self,
        label: str,
        value: float,
    ):

        self.labels.append(label)

        self.values.append(value)
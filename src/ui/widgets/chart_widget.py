"""
PresentationAI

Chart Property Widget
"""

from __future__ import annotations

from PySide6.QtWidgets import (
    QLabel,
    QVBoxLayout,
    QWidget,
)

from src.models.elements.chart_element import ChartElement


class ChartWidget(QWidget):
    """
    Chart element properties.

    Placeholder for Release 0.6
    """

    # -------------------------------------------------

    def __init__(self, app):

        super().__init__()

        self.app = app

        self._element = None

        layout = QVBoxLayout(self)

        layout.addWidget(
            QLabel("Chart Properties")
        )

        layout.addStretch()

    # -------------------------------------------------

    def load(
        self,
        element: ChartElement,
    ):

        self._element = element

    # -------------------------------------------------

    def clear(self):

        self._element = None
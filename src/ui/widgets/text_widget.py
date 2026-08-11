"""
PresentationAI

Text Property Widget
"""

from __future__ import annotations

from PySide6.QtWidgets import (
    QLabel,
    QVBoxLayout,
    QWidget,
)


class TextWidget(QWidget):
    """
    Text element properties.

    Placeholder for Release 0.6
    """

    # -------------------------------------------------

    def __init__(self, app):

        super().__init__()

        self.app = app

        layout = QVBoxLayout(self)

        layout.addWidget(
            QLabel("Text Properties")
        )

        layout.addStretch()

    # -------------------------------------------------

    def load(self, element):

        pass

    # -------------------------------------------------

    def clear(self):

        pass
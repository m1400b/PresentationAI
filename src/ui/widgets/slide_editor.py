"""
PresentationAI

Slide Editor
"""

from __future__ import annotations

from PySide6.QtWidgets import (
    QWidget,
    QHBoxLayout,
    QVBoxLayout,
)

from src.ui.widgets.editor_toolbar import EditorToolBar
from src.ui.widgets.slide_preview import SlidePreviewWidget
from src.ui.widgets.property_panel import PropertyPanel

from src.models.slide import Slide


class SlideEditor(QWidget):

    # -------------------------------------------------

    def __init__(self, app):

        super().__init__()

        self.app = app

        self.build_ui()

    # -------------------------------------------------

    def build_ui(self):

        root = QHBoxLayout(self)

        root.setContentsMargins(
            0,
            0,
            0,
            0,
        )

        root.setSpacing(8)

        #
        # Left Side
        #

        left = QVBoxLayout()

        left.setContentsMargins(
            0,
            0,
            0,
            0,
        )

        left.setSpacing(8)

        #
        # Toolbar
        #

        self.toolbar = EditorToolBar(
            self.app
        )

        left.addWidget(
            self.toolbar
        )

        #
        # Canvas
        #

        self.canvas = SlidePreviewWidget(
            self.app
        )

        left.addWidget(
            self.canvas,
            1,
        )

        #
        # Right Side
        #

        self.properties = PropertyPanel(
            self.app
        )

        #
        # Layout
        #

        root.addLayout(
            left,
            4,
        )

        root.addWidget(
            self.properties,
            2,
        )

    # -------------------------------------------------

    def set_slide(
        self,
        slide: Slide | None,
    ):

        #
        # Canvas
        #

        self.canvas.set_slide(
            slide
        )

        #
        # Property Panel
        #

        self.properties.reload()

    # -------------------------------------------------

    def clear(self):

        self.set_slide(None)

    # -------------------------------------------------

    def refresh(self):

        self.canvas.update()

        self.properties.reload()

    # -------------------------------------------------

    def current_slide(self):

        return self.app.selection.current_slide

    # -------------------------------------------------

    def current_element(self):

        return self.app.selection.current_element
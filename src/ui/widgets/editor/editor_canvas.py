"""
PresentationAI

Editor Canvas
"""

from PySide6.QtWidgets import QWidget
from PySide6.QtVBoxLayout import QVBoxLayout

from src.ui.widgets.slide_preview import SlidePreviewWidget


class EditorCanvas(QWidget):

    def __init__(self, app):

        super().__init__()

        layout = QVBoxLayout(self)

        layout.setContentsMargins(0, 0, 0, 0)

        self.preview = SlidePreviewWidget(app)

        layout.addWidget(self.preview)

    def set_slide(self, slide):

        self.preview.set_slide(slide)
"""
PresentationAI

Slides Page
"""

from PySide6.QtWidgets import (
    QWidget,
    QListWidget,
    QPushButton,
    QLabel,
    QVBoxLayout,
    QHBoxLayout,
)

from src.services.slide_service import SlideService
from src.services.slide_renderer import SlideRenderer

from src.ui.widgets.slide_editor import SlideEditor


class SlidesPage(QWidget):

    # -------------------------------------------------

    def __init__(self, app):

        super().__init__()

        self.app = app

        self.services = app.services

        self.slide_service = self.services.get(
            SlideService
        )

        self.renderer = SlideRenderer()

        self.build_ui()

    # -------------------------------------------------

    def build_ui(self):

        root = QHBoxLayout(self)

        # ==========================================
        # Left Panel
        # ==========================================

        left = QVBoxLayout()

        title = QLabel("Slides")

        title.setStyleSheet("""
            font-size:22px;
            font-weight:bold;
        """)

        left.addWidget(title)

        toolbar = QHBoxLayout()

        self.btn_add = QPushButton("Add")
        self.btn_delete = QPushButton("Delete")
        self.btn_duplicate = QPushButton("Duplicate")

        toolbar.addWidget(self.btn_add)
        toolbar.addWidget(self.btn_delete)
        toolbar.addWidget(self.btn_duplicate)

        left.addLayout(toolbar)

        self.slide_list = QListWidget()

        left.addWidget(
            self.slide_list,
            1,
        )

        # ==========================================
        # Right Panel
        # ==========================================

        self.editor = SlideEditor(
            self.app
        )

        root.addLayout(
            left,
            2,
        )

        root.addWidget(
            self.editor,
            5,
        )

        # ==========================================
        # Signals
        # ==========================================

        self.btn_add.clicked.connect(
            self.add_slide
        )

        self.btn_delete.clicked.connect(
            self.delete_slide
        )

        self.slide_list.currentRowChanged.connect(
            self.slide_selected
        )

        self.refresh()

    # -------------------------------------------------

    def refresh(self):

        current = self.slide_list.currentRow()

        self.slide_list.blockSignals(True)

        self.slide_list.clear()

        for slide in self.slide_service.slides:

            self.slide_list.addItem(
                f"📄 {slide.order:02d}    {slide.title}"
            )

        self.slide_list.blockSignals(False)

        if self.slide_list.count() == 0:

            self.editor.clear()

            return

        if current < 0:

            current = 0

        if current >= self.slide_list.count():

            current = self.slide_list.count() - 1

        self.slide_list.setCurrentRow(current)

    # -------------------------------------------------

    def add_slide(self):

        slide = self.slide_service.add_slide()

        self.renderer.render(slide)

        self.slide_service.save_slide(slide)

        self.refresh()

        self.slide_list.setCurrentRow(
            self.slide_list.count() - 1
        )

    # -------------------------------------------------

    def delete_slide(self):

        row = self.slide_list.currentRow()

        if row < 0:

            return

        self.slide_service.delete_slide(row)

        self.refresh()

    # -------------------------------------------------

    def duplicate_slide(self):

        row = self.slide_list.currentRow()

        if row < 0:

            return

        self.slide_service.duplicate_slide(row)

        self.refresh()

    # -------------------------------------------------

    def slide_selected(self, row):

        if row < 0:

            self.app.selection.set_slide(None)

            self.editor.clear()

            return

        slide = self.slide_service.get(row)

        if slide is None:

            self.app.selection.set_slide(None)

            self.editor.clear()

            return

        self.app.selection.set_slide(
            slide
        )

        self.editor.set_slide(
            slide
        )

    # -------------------------------------------------

    def current_slide(self):

        row = self.slide_list.currentRow()

        if row < 0:

            return None

        return self.slide_service.get(row)
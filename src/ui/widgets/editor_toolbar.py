"""
PresentationAI

Editor Toolbar
"""

from __future__ import annotations

from PySide6.QtCore import Signal

from PySide6.QtWidgets import (
    QWidget,
    QHBoxLayout,
    QPushButton,
)


class EditorToolBar(QWidget):

    """
    Slide editor toolbar.

    This widget only emits signals.
    It does NOT manipulate models directly.
    """

    # -------------------------------------------------
    # Signals
    # -------------------------------------------------

    add_text_requested = Signal()

    add_image_requested = Signal()

    add_chart_requested = Signal()

    delete_requested = Signal()

    duplicate_requested = Signal()

    copy_requested = Signal()

    paste_requested = Signal()

    undo_requested = Signal()

    redo_requested = Signal()

    bring_front_requested = Signal()

    send_back_requested = Signal()

    # -------------------------------------------------

    def __init__(self, app):

        super().__init__()

        self.app = app

        self.build_ui()

    # -------------------------------------------------

    def build_ui(self):

        layout = QHBoxLayout(self)

        layout.setContentsMargins(4, 4, 4, 4)

        layout.setSpacing(4)

        #
        # Add
        #

        self.btn_text = QPushButton("Text")

        self.btn_image = QPushButton("Image")

        self.btn_chart = QPushButton("Chart")

        #
        # Clipboard
        #

        self.btn_copy = QPushButton("Copy")

        self.btn_paste = QPushButton("Paste")

        #
        # Element
        #

        self.btn_duplicate = QPushButton("Duplicate")

        self.btn_delete = QPushButton("Delete")

        #
        # History
        #

        self.btn_undo = QPushButton("Undo")

        self.btn_redo = QPushButton("Redo")

        #
        # Z Order
        #

        self.btn_front = QPushButton("Front")

        self.btn_back = QPushButton("Back")

        #
        # Layout
        #

        layout.addWidget(self.btn_text)

        layout.addWidget(self.btn_image)

        layout.addWidget(self.btn_chart)

        layout.addSpacing(10)

        layout.addWidget(self.btn_copy)

        layout.addWidget(self.btn_paste)

        layout.addSpacing(10)

        layout.addWidget(self.btn_duplicate)

        layout.addWidget(self.btn_delete)

        layout.addSpacing(10)

        layout.addWidget(self.btn_front)

        layout.addWidget(self.btn_back)

        layout.addSpacing(10)

        layout.addWidget(self.btn_undo)

        layout.addWidget(self.btn_redo)

        layout.addStretch()

        #
        # Connections
        #

        self.btn_text.clicked.connect(
            self.add_text_requested
        )

        self.btn_image.clicked.connect(
            self.add_image_requested
        )

        self.btn_chart.clicked.connect(
            self.add_chart_requested
        )

        self.btn_copy.clicked.connect(
            self.copy_requested
        )

        self.btn_paste.clicked.connect(
            self.paste_requested
        )

        self.btn_duplicate.clicked.connect(
            self.duplicate_requested
        )

        self.btn_delete.clicked.connect(
            self.delete_requested
        )

        self.btn_front.clicked.connect(
            self.bring_front_requested
        )

        self.btn_back.clicked.connect(
            self.send_back_requested
        )

        self.btn_undo.clicked.connect(
            self.undo_requested
        )

        self.btn_redo.clicked.connect(
            self.redo_requested
        )

    # -------------------------------------------------

    def set_enabled(
        self,
        enabled: bool,
    ):

        for button in self.findChildren(QPushButton):

            button.setEnabled(enabled)
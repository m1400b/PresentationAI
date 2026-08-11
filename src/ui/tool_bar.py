"""
PresentationAI Toolbar
"""

from PySide6.QtCore import Qt
from PySide6.QtGui import QAction
from PySide6.QtWidgets import QToolBar


def build_tool_bar(parent) -> QToolBar:
    """
    Creates the main application toolbar.
    """

    toolbar = QToolBar("Main Toolbar", parent)

    toolbar.setMovable(False)
    toolbar.setFloatable(False)

    toolbar.setToolButtonStyle(
        Qt.ToolButtonTextUnderIcon
    )

    # -------------------------------------------------
    # Project
    # -------------------------------------------------

    action_new = QAction("New", parent)
    action_new.triggered.connect(
        parent.new_project
    )

    action_open = QAction("Open", parent)
    action_open.triggered.connect(
        parent.open_project
    )

    action_save = QAction("Save", parent)
    action_save.triggered.connect(
        parent.save_project
    )

    # -------------------------------------------------
    # AI
    # -------------------------------------------------

    action_generate = QAction(
        "Generate AI",
        parent,
    )

    action_generate.triggered.connect(
        parent.generate_presentation
    )

    # -------------------------------------------------
    # Export
    # -------------------------------------------------

    action_export = QAction(
        "Export PPTX",
        parent,
    )

    action_export.triggered.connect(
        parent.export_presentation
    )

    # -------------------------------------------------
    # Toolbar
    # -------------------------------------------------

    toolbar.addAction(action_new)
    toolbar.addAction(action_open)
    toolbar.addAction(action_save)

    toolbar.addSeparator()

    toolbar.addAction(action_generate)

    toolbar.addSeparator()

    toolbar.addAction(action_export)

    return toolbar
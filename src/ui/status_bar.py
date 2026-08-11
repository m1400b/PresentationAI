"""
PresentationAI

Status Bar
"""

from PySide6.QtWidgets import QLabel, QStatusBar


def build_status_bar() -> QStatusBar:
    """
    Creates the application's status bar.
    """

    status = QStatusBar()

    status.showMessage("Ready")

    version = QLabel("Version 0.2.0")

    status.addPermanentWidget(version)

    return status
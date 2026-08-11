"""
PresentationAI

Base Page
"""

from PySide6.QtCore import Qt
from PySide6.QtWidgets import (
    QWidget,
    QLabel,
    QVBoxLayout,
)


class BasePage(QWidget):

    def __init__(self, title, subtitle=""):

        super().__init__()

        layout = QVBoxLayout(self)

        layout.addStretch()

        lbl_title = QLabel(title)

        lbl_title.setAlignment(Qt.AlignCenter)

        lbl_title.setStyleSheet("""

            font-size:28px;

            font-weight:bold;

        """)

        layout.addWidget(lbl_title)

        if subtitle:

            lbl_subtitle = QLabel(subtitle)

            lbl_subtitle.setAlignment(Qt.AlignCenter)

            lbl_subtitle.setStyleSheet("""

                font-size:15px;

                color:gray;

            """)

            layout.addWidget(lbl_subtitle)

        layout.addStretch()
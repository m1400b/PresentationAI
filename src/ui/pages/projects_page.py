from PySide6.QtCore import Qt
from PySide6.QtWidgets import (
    QWidget,
    QLabel,
    QPushButton,
    QListWidget,
    QVBoxLayout,
    QHBoxLayout,
)


class ProjectsPage(QWidget):

    def __init__(self):

        super().__init__()

        layout = QVBoxLayout(self)

        title = QLabel("📁 Projects")

        title.setAlignment(Qt.AlignCenter)

        title.setStyleSheet("""

            font-size:24px;

            font-weight:bold;

        """)

        layout.addWidget(title)

        buttons = QHBoxLayout()

        self.btn_new = QPushButton("New")

        self.btn_open = QPushButton("Open")

        buttons.addWidget(self.btn_new)

        buttons.addWidget(self.btn_open)

        buttons.addStretch()

        layout.addLayout(buttons)

        self.recent = QListWidget()

        layout.addWidget(self.recent)
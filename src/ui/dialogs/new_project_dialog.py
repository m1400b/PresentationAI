"""
PresentationAI

New Project Dialog
"""

from PySide6.QtWidgets import (
    QDialog,
    QVBoxLayout,
    QHBoxLayout,
    QLabel,
    QLineEdit,
    QPushButton,
    QFileDialog
)


class NewProjectDialog(QDialog):

    def __init__(self, parent=None):

        super().__init__(parent)

        self.setWindowTitle("New Project")

        self.resize(500, 140)

        self.project_name = QLineEdit()

        self.project_location = QLineEdit()

        browse = QPushButton("Browse...")

        browse.clicked.connect(self.select_folder)

        layout = QVBoxLayout(self)

        layout.addWidget(QLabel("Project Name"))

        layout.addWidget(self.project_name)

        layout.addWidget(QLabel("Location"))

        row = QHBoxLayout()

        row.addWidget(self.project_location)

        row.addWidget(browse)

        layout.addLayout(row)

        buttons = QHBoxLayout()

        ok = QPushButton("Create")

        cancel = QPushButton("Cancel")

        ok.clicked.connect(self.accept)

        cancel.clicked.connect(self.reject)

        buttons.addStretch()

        buttons.addWidget(ok)

        buttons.addWidget(cancel)

        layout.addLayout(buttons)

    # ---------------------------------------------

    def select_folder(self):

        folder = QFileDialog.getExistingDirectory(
            self,
            "Project Location"
        )

        if folder:

            self.project_location.setText(folder)
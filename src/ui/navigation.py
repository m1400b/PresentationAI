"""
Navigation Panel
"""

from PySide6.QtWidgets import (
    QListWidget,
    QListWidgetItem,
    QVBoxLayout,
    QWidget,
)


class NavigationPanel(QWidget):
    """
    Left navigation panel.
    """

    def __init__(self):

        super().__init__()

        self.setMinimumWidth(240)
        self.setMaximumWidth(280)

        self.build_ui()

    def build_ui(self):

        layout = QVBoxLayout()

        self.setLayout(layout)

        self.list = QListWidget()

        pages = [

            "🏠 Dashboard",

            "📁 Projects",

            "📝 Presentation",

            "📄 Slides",

            "🎨 Themes",

            "🧩 Templates",

            "🤖 AI",

            "📚 Assets",

            "⚙ Settings",

            "ℹ About"

        ]

        for page in pages:

            QListWidgetItem(page, self.list)

        self.list.setCurrentRow(0)

        layout.addWidget(self.list)
        
    # ------------------------------------------------

    def current_page(self):

        return self.list.currentRow()
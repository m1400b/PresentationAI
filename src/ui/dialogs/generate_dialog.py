"""
PresentationAI

Generate Presentation Dialog
"""

from __future__ import annotations

from PySide6.QtCore import Qt
from src.ai.prompt_builder import PromptRequest
from PySide6.QtWidgets import (
    QDialog,
    QVBoxLayout,
    QHBoxLayout,
    QFormLayout,
    QLabel,
    QLineEdit,
    QTextEdit,
    QComboBox,
    QSpinBox,
    QSlider,
    QCheckBox,
    QPushButton,
    QWidget,
    QTabWidget,
    QDialogButtonBox,
    QGroupBox,
)

class GenerateDialog(QDialog):

    # -------------------------------------------------

    def __init__(self, parent=None):

        super().__init__(parent)

        self.setWindowTitle(
            "Generate Presentation"
        )

        self.resize(720, 650)

        self.build_ui()
        
        # -------------------------------------------------

    def build_ui(self):

        layout = QVBoxLayout(self)

        #
        # Tabs
        #

        self.tabs = QTabWidget()

        layout.addWidget(self.tabs)

        #
        # Pages
        #

        self.general_tab = QWidget()

        self.presentation_tab = QWidget()

        self.ai_tab = QWidget()

        self.content_tab = QWidget()

        self.tabs.addTab(
            self.general_tab,
            "General",
        )

        self.tabs.addTab(
            self.presentation_tab,
            "Presentation",
        )

        self.tabs.addTab(
            self.ai_tab,
            "AI",
        )

        self.tabs.addTab(
            self.content_tab,
            "Content",
        )

        #
        # Build Pages
        #

        self.build_general_tab()

        self.build_presentation_tab()

        self.build_ai_tab()

        self.build_content_tab()

        #
        # Buttons
        #

        buttons = QDialogButtonBox(

            QDialogButtonBox.Ok
            |
            QDialogButtonBox.Cancel

        )

        buttons.accepted.connect(
            self.accept
        )

        buttons.rejected.connect(
            self.reject
        )

        layout.addWidget(buttons)
    
        # -------------------------------------------------

    def build_general_tab(self):

        layout = QFormLayout(
            self.general_tab
        )

        #
        # Topic
        #

        self.topic_edit = QLineEdit()

        layout.addRow(
            "Topic",
            self.topic_edit,
        )

        #
        # Prompt
        #

        self.prompt_edit = QTextEdit()

        self.prompt_edit.setMinimumHeight(
            140
        )

        layout.addRow(
            "Prompt",
            self.prompt_edit,
        )

        #
        # Slide Count
        #

        self.slide_count = QSpinBox()

        self.slide_count.setRange(
            1,
            100,
        )

        self.slide_count.setValue(10)

        layout.addRow(
            "Slides",
            self.slide_count,
        )

        #
        # Language
        #

        self.language = QComboBox()

        self.language.addItems(

            [

                "Persian",

                "English",

                "Arabic",

            ]

        )

        layout.addRow(
            "Language",
            self.language,
        )
    
        # -------------------------------------------------

    def build_presentation_tab(self):

        layout = QFormLayout(
            self.presentation_tab
        )

        #
        # Audience
        #

        self.audience = QComboBox()

        self.audience.addItems(

            [

                "General",

                "Students",

                "Managers",

                "Executives",

                "Customers",

            ]

        )

        layout.addRow(
            "Audience",
            self.audience,
        )

        #
        # Purpose
        #

        self.purpose = QComboBox()

        self.purpose.addItems(

            [

                "Education",

                "Training",

                "Meeting",

                "Pitch",

                "Marketing",

            ]

        )

        layout.addRow(
            "Purpose",
            self.purpose,
        )

        #
        # Style
        #

        self.style = QComboBox()

        self.style.addItems(

            [

                "Professional",

                "Modern",

                "Minimal",

                "Academic",

                "Creative",

            ]

        )

        layout.addRow(
            "Style",
            self.style,
        )

        #
        # Theme
        #

        self.theme = QComboBox()

        self.theme.addItems(

            [

                "Corporate",

                "Dark",

                "Light",

                "Minimal",

            ]

        )

        layout.addRow(
            "Theme",
            self.theme,
        )
    
        # -------------------------------------------------

    def build_ai_tab(self):

        layout = QVBoxLayout(
            self.ai_tab
        )

        #
        # Provider
        #

        provider_group = QGroupBox(
            "AI Provider"
        )

        form = QFormLayout(
            provider_group
        )

        self.provider = QComboBox()

        self.provider.addItems(

            [

                "Auto",

                "Fake",

                "Ollama",

                "OpenAI",

                "Gemini",

                "Claude",

                "LM Studio",

            ]

        )

        form.addRow(
            "Provider",
            self.provider,
        )

        layout.addWidget(
            provider_group
        )

        #
        # Creativity
        #

        creativity_group = QGroupBox(
            "Creativity"
        )

        v = QVBoxLayout(
            creativity_group
        )

        self.creativity = QSlider(
            Qt.Horizontal
        )

        self.creativity.setRange(
            0,
            100,
        )

        self.creativity.setValue(
            50,
        )

        self.creativity_label = QLabel(
            "Balanced"
        )

        self.creativity.valueChanged.connect(
            self._update_creativity_label
        )

        v.addWidget(
            self.creativity
        )

        v.addWidget(
            self.creativity_label
        )

        layout.addWidget(
            creativity_group
        )

        #
        # AI Options
        #

        options = QGroupBox(
            "Options"
        )

        box = QVBoxLayout(
            options
        )

        self.allow_online = QCheckBox(
            "Allow Internet Providers"
        )

        self.allow_online.setChecked(
            True
        )

        self.offline_only = QCheckBox(
            "Offline Only"
        )

        self.offline_only.setChecked(
            False
        )

        box.addWidget(
            self.allow_online
        )

        box.addWidget(
            self.offline_only
        )

        layout.addWidget(
            options
        )

        layout.addStretch()
        
        # -------------------------------------------------

    def build_content_tab(self):

        layout = QVBoxLayout(
            self.content_tab
        )

        #
        # Generated Content
        #

        group = QGroupBox(
            "Generated Content"
        )

        box = QVBoxLayout(
            group
        )

        self.include_images = QCheckBox(
            "Suggest Images"
        )

        self.include_images.setChecked(
            True
        )

        self.include_charts = QCheckBox(
            "Generate Charts"
        )

        self.include_charts.setChecked(
            True
        )

        self.include_tables = QCheckBox(
            "Generate Tables"
        )

        self.include_notes = QCheckBox(
            "Speaker Notes"
        )

        self.include_notes.setChecked(
            True
        )

        self.include_references = QCheckBox(
            "References"
        )

        self.include_agenda = QCheckBox(
            "Agenda Slide"
        )

        self.include_summary = QCheckBox(
            "Summary Slide"
        )

        self.include_thankyou = QCheckBox(
            "Thank You Slide"
        )

        box.addWidget(
            self.include_images
        )

        box.addWidget(
            self.include_charts
        )

        box.addWidget(
            self.include_tables
        )

        box.addWidget(
            self.include_notes
        )

        box.addWidget(
            self.include_references
        )

        box.addWidget(
            self.include_agenda
        )

        box.addWidget(
            self.include_summary
        )

        box.addWidget(
            self.include_thankyou
        )

        layout.addWidget(
            group
        )

        #
        # Extra Instructions
        #

        extra_group = QGroupBox(
            "Additional Instructions"
        )

        extra_layout = QVBoxLayout(
            extra_group
        )

        self.extra = QTextEdit()

        self.extra.setPlaceholderText(

            "Example:\n"

            "Use official statistics.\n"

            "RTL layout.\n"

            "Minimal design."

        )

        self.extra.setMinimumHeight(
            140
        )

        extra_layout.addWidget(
            self.extra
        )

        layout.addWidget(
            extra_group
        )
        # -------------------------------------------------

    def _update_creativity_label(
        self,
        value,
    ):

        if value < 20:

            text = "Very Precise"

        elif value < 40:

            text = "Precise"

        elif value < 60:

            text = "Balanced"

        elif value < 80:

            text = "Creative"

        else:

            text = "Very Creative"

        self.creativity_label.setText(
            text
        )
        # -------------------------------------------------

    def request(self) -> PromptRequest:

        return PromptRequest(

            topic=self.topic_edit.text().strip(),

            prompt=self.prompt_edit.toPlainText().strip(),

            slide_count=self.slide_count.value(),

            language=self.language.currentText(),

            audience=self.audience.currentText(),

            purpose=self.purpose.currentText(),

            style=self.style.currentText(),

            theme=self.theme.currentText(),

            provider=self.provider.currentText(),

            creativity=self.creativity.value(),

            allow_online=self.allow_online.isChecked(),

            offline_only=self.offline_only.isChecked(),

            include_images=self.include_images.isChecked(),

            include_charts=self.include_charts.isChecked(),

            include_tables=self.include_tables.isChecked(),

            include_notes=self.include_notes.isChecked(),

            include_references=self.include_references.isChecked(),

            include_agenda=self.include_agenda.isChecked(),

            include_summary=self.include_summary.isChecked(),

            include_thankyou=self.include_thankyou.isChecked(),

            extra=self.extra.toPlainText().strip(),

        )
        # -------------------------------------------------

    def accept(self):

        if not self.topic_edit.text().strip():

            self.topic_edit.setFocus()

            return

        super().accept()
    
        # -------------------------------------------------

    def topic(self):

        return self.topic_edit.text().strip()

    # -------------------------------------------------

    def prompt(self):

        return self.prompt_edit.toPlainText().strip()

    # -------------------------------------------------

    def count(self):

        return self.slide_count.value()
    
"""
PresentationAI

Main Window
"""
from src.ui.dialogs.generate_dialog import GenerateDialog
from src.ai.prompt_builder import PromptRequest
from PySide6.QtCore import Qt
from PySide6.QtWidgets import (
    QMainWindow,
    QWidget,
    QHBoxLayout,
    QMessageBox,
    QFileDialog,
    QDialog,
)
from src.services.slide_service import SlideService
from src.ui.menu_bar import build_menu_bar
from src.ui.tool_bar import build_tool_bar
from src.ui.navigation import NavigationPanel
from src.ui.workspace import Workspace
from src.ui.status_bar import build_status_bar
from src.services.presentation_service import PresentationService
from src.services.export_service import ExportService

from src.services.logger_service import LoggerService
from src.services.project_service import ProjectService

from src.ui.dialogs.new_project_dialog import NewProjectDialog


class MainWindow(QMainWindow):

    # -------------------------------------------------

    def __init__(self, app):

        super().__init__()

        self.app = app

        self.services = app.services

        self.events = app.events

        self.logger = self.services.get(LoggerService)

        self.project_service = self.services.get(
    ProjectService
        )

        self.slide_service = self.services.get(
            SlideService
        )

        self.presentation_service = self.services.get(
            PresentationService
        )

        self.export_service = self.services.get(
            ExportService
        )


        self.setWindowTitle("PresentationAI")

        self.resize(1400, 850)

        self.logger.info("Creating MainWindow...")

        try:

            self.initialize_ui()

            self.logger.info("MainWindow created.")

        except Exception:

            self.logger.exception(
                "MainWindow initialization failed."
            )

            raise

    # -------------------------------------------------
    def initialize_ui(self):

        self.logger.debug("Building MenuBar")
        self.setMenuBar(build_menu_bar(self))

        self.logger.debug("Building ToolBar")
        self.addToolBar(
            Qt.TopToolBarArea,
            build_tool_bar(self)
        )

        self.logger.debug("Building StatusBar")
        self.setStatusBar(build_status_bar())

        self.logger.debug("Creating CentralWidget")

        central = QWidget()
        self.setCentralWidget(central)

        layout = QHBoxLayout(central)
        layout.setContentsMargins(5, 5, 5, 5)
        layout.setSpacing(5)

        self.logger.debug("Creating NavigationPanel")
        self.navigation = NavigationPanel()
        layout.addWidget(self.navigation)

        self.logger.debug("Creating Workspace")
        self.workspace = Workspace(self.app)
        layout.addWidget(self.workspace, 1)

        self.navigation.list.currentRowChanged.connect(
            self.workspace.show_page
        )

        self.logger.debug("MainWindow UI Ready")

    # -------------------------------------------------

    def refresh_title(self):

        project = self.project_service.current_project

        if project:

            self.setWindowTitle(

                f"PresentationAI - {project.name}"

            )

        else:

            self.setWindowTitle("PresentationAI")

    # -------------------------------------------------

    def new_project(self):

        dialog = NewProjectDialog(self)

        if dialog.exec() != QDialog.DialogCode.Accepted:

            return

        name = dialog.project_name.text().strip()

        location = dialog.project_location.text().strip()

        if not name:

            QMessageBox.warning(

                self,

                "PresentationAI",

                "Project name is required."

            )

            return

        if not location:

            QMessageBox.warning(

                self,

                "PresentationAI",

                "Project location is required."

            )

            return

        try:

            project = self.project_service.create_project(

                name,

                location

            )

            self.refresh_title()

            self.events.emit(

                "project_created",

                project

            )

            self.logger.info(

                f'Project "{project.name}" created.'

            )

            QMessageBox.information(

                self,

                "PresentationAI",

                "Project created successfully."

            )

        except Exception as e:

            self.logger.exception(
                "Cannot create project."
            )

            QMessageBox.critical(
                self,
                "PresentationAI",
                str(e)
            )

    # -------------------------------------------------

    def open_project(self):

        folder = QFileDialog.getExistingDirectory(

            self,

            "Open Project"

        )

        if not folder:

            return

        try:

            project = self.project_service.load_project(

                folder

            )

            self.refresh_title()

            self.events.emit(

                "project_created",

                project

            )

            self.logger.info(

                f'Project "{project.name}" opened.'

            )

        except Exception as e:

            self.logger.exception(
                "Cannot open project."
            )

            QMessageBox.critical(
                self,
                "PresentationAI",
                str(e)
            )

    # -------------------------------------------------

    def save_project(self):

        if not self.project_service.project_is_open():

            QMessageBox.information(

                self,

                "PresentationAI",

                "No project is open."

            )

            return

        try:

            self.project_service.save_project()

            self.logger.info(

                "Project saved."

            )

            QMessageBox.information(

                self,

                "PresentationAI",

                "Project saved."

            )

        except Exception as e:

            self.logger.exception(
                "Cannot save project."
            )

            QMessageBox.critical(
                self,
                "PresentationAI",
                str(e)
            )
            
    def generate_presentation(self):

        dialog = GenerateDialog(self)

        if dialog.exec() != QDialog.DialogCode.Accepted:

            return

        if not dialog.topic():

            return

        request = dialog.request()

        slides = self.presentation_service.generate(request)
        
        self.workspace.slides_page.refresh()

        self.workspace.slides_page.slide_list.setCurrentRow(0)

        QMessageBox.information(
        
            self,

            "PresentationAI",

            f"{len(slides)} slide(s) generated.",

        )
        #
        # TODO
        #

        # Refresh Slides Panel
        # Refresh Canvas
        # Refresh Properties   
        
    def export_presentation(self):

        filename, _ = QFileDialog.getSaveFileName(

            self,

            "Export Presentation",

            "presentation.pptx",

            "PowerPoint (*.pptx)",

        )

        if not filename:

            return

        ok = self.export_service.export_pptx(
            filename
        )

        if ok:

            QMessageBox.information(

                self,

                "PresentationAI",

                "Presentation exported successfully.",

            )

        else:

            QMessageBox.critical(

                self,

                "PresentationAI",

                "Export failed.",

            )
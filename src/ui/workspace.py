"""
PresentationAI

Workspace
"""

from PySide6.QtWidgets import (
    QFrame,
    QVBoxLayout,
    QStackedWidget,
)

from src.services.logger_service import LoggerService

from src.ui.pages.dashboard_page import DashboardPage
from src.ui.pages.projects_page import ProjectsPage
from src.ui.pages.presentation_page import PresentationPage
from src.ui.pages.slides_page import SlidesPage
from src.ui.pages.themes_page import ThemesPage
from src.ui.pages.templates_page import TemplatesPage
from src.ui.pages.ai_page import AIPage
from src.ui.pages.assets_page import AssetsPage
from src.ui.pages.settings_page import SettingsPage
from src.ui.pages.about_page import AboutPage


class Workspace(QFrame):

    def __init__(self, app):

        super().__init__()

        self.app = app
        self.services = app.services
        self.events = app.events

        self.logger = self.services.get(LoggerService)

        self.build_ui()

    # ------------------------------------------------

    def build_ui(self):

        self.logger.debug("Workspace : building")

        layout = QVBoxLayout(self)
        layout.setContentsMargins(0, 0, 0, 0)

        self.stack = QStackedWidget()

        layout.addWidget(self.stack)

        self.dashboard_page = DashboardPage()

        self.projects_page = ProjectsPage()
        
        self.presentation_page = PresentationPage()
        
        self.slides_page = SlidesPage(self.app)
        
        self.themes_page = ThemesPage()
        
        self.templates_page = TemplatesPage()
        
        self.ai_page = AIPage()
        
        self.assets_page = AssetsPage()
        
        self.settings_page = SettingsPage()
        
        self.about_page = AboutPage()
        
        self.pages = [
        
        self.dashboard_page,
    
        self.projects_page,
    
        self.presentation_page,
    
        self.slides_page,
    
        self.themes_page,
    
        self.templates_page,
    
        self.ai_page,
    
        self.assets_page,
    
        self.settings_page,
    
        self.about_page,

]
        

        for page in self.pages:

            self.logger.debug(
                f"Loading page : {page.__class__.__name__}"
            )

            self.stack.addWidget(page)

        self.logger.debug("Workspace ready")

    # ------------------------------------------------

    def show_page(self, index):

        if 0 <= index < self.stack.count():

            self.stack.setCurrentIndex(index)
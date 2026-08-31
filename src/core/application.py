"""
PresentationAI

Application
"""

import sys
import traceback
from src.repositories.element_repository import ElementRepository
from PySide6.QtWidgets import QApplication
from themes.base_theme import BaseTheme
from src.core.service_container import ServiceContainer
from src.core.event_bus import EventBus

from src.database.database_service import DatabaseService

from src.repositories.project_repository import ProjectRepository
from src.repositories.slide_repository import SlideRepository
from src.ai.layout_registry import (
    LayoutRegistry,
)
from src.services.logger_service import LoggerService
from src.services.config_service import ConfigService
from src.services.version_service import VersionService
from src.services.language_service import LanguageService

from src.services.project_service import ProjectService
from src.services.slide_service import SlideService

from src.services.presentation_service import PresentationService

from src.ai.layout_registry import LayoutRegistry
from src.services.layout_engine import LayoutEngine
from src.services.export_service import ExportService
from src.services.selection_manager import SelectionManager
from src.services.element_service import ElementService
from src.ui.main_window import MainWindow
from src.ai.ai_client import AIClient
from src.ai.providers.provider_manager import ProviderManager
from src.ai.providers.fake_ai_provider import FakeAIProvider
from src.services.settings_service import (
    SettingsService,
)

class Application:

    def __init__(self):

        self.qt = QApplication(sys.argv)

        self.services = ServiceContainer()

        self.events = EventBus()
        self.selection = SelectionManager()
        self.services.register(SelectionManager,self.selection,)
        element_service = ElementService()

        element_service.initialize()
        
        self.services.register(
            ElementService,
            element_service,
        )
        
        

        self.window = None

    # -------------------------------------------------

    def initialize(self):

        logger = LoggerService()

        logger.initialize()

        self.services.register(
            LoggerService,
            logger,
        )

        try:

            # -----------------------------------------
            # Config
            # -----------------------------------------

            config = ConfigService()
            config.initialize()

            self.services.register(
                ConfigService,
                config,
            )
            # -----------------------------------------
            # Settings
            # -----------------------------------------

            settings = SettingsService()

            settings.initialize()

            self.services.register(
            
                SettingsService,

                settings,

            )

            # -----------------------------------------
            # Version
            # -----------------------------------------

            version = VersionService()
            version.initialize()

            self.services.register(
                VersionService,
                version,
            )

            # -----------------------------------------
            # Language
            # -----------------------------------------

            language = LanguageService()
            language.initialize()

            self.services.register(
                LanguageService,
                language,
            )

            # -----------------------------------------
            # Database
            # -----------------------------------------

            database = DatabaseService()
            database.initialize()

            self.services.register(
                DatabaseService,
                database,
            )

            # -----------------------------------------
            # Repositories
            # -----------------------------------------

            project_repository = ProjectRepository(
                database
            )

            slide_repository = SlideRepository(
                database
            )
            element_repository = ElementRepository(
    database
)
            self.services.register(
                ProjectRepository,
                project_repository,
            )

            self.services.register(
                SlideRepository,
                slide_repository,
            )
            
            self.services.register(
    ElementRepository,
    element_repository,
)

            # =========================================
            # Slide Service
            # باید قبل از ProjectService ساخته شود
            # =========================================

            slide_service = SlideService(
    slide_repository,
    element_repository,
)

            slide_service.initialize()

            self.services.register(
                SlideService,
                slide_service,
            )

            # =========================================
            # Project Service
            # =========================================

            project_service = ProjectService(
                project_repository,
                slide_service,
            )
            slide_service.project_service = project_service
            project_service.initialize()

            self.services.register(
                ProjectService,
                project_service,
            )

            

            # -----------------------------------------
            # Layout Registry
            # -----------------------------------------

            layout_registry = LayoutRegistry()

            self.services.register(
                LayoutRegistry,
                layout_registry,
            )

            # -----------------------------------------
            # Layout Engine
            # -----------------------------------------

            layout_engine = LayoutEngine(
                layout_registry,
            )

            self.services.register(
                LayoutEngine,
                layout_engine,
            )

            # -----------------------------------------
            # Theme
            # -----------------------------------------

            theme = BaseTheme()

            self.services.register(
                BaseTheme,
                theme,
            )
            # -----------------------------------------
            # Provider Manager
            # -----------------------------------------

            provider_manager = ProviderManager()

            self.register_ai_providers(
                provider_manager,
            )

            self.services.register(
                ProviderManager,
                provider_manager,
            )
            
            # -----------------------------------------
            # AI Client
            # -----------------------------------------
            
            ai_client = AIClient(
                provider_manager
            )

            self.services.register(
            AIClient,
            ai_client,
        )

            # -----------------------------------------
            # Presentation Service
            # -----------------------------------------

            presentation_service = PresentationService(
            slide_service,
            layout_engine,
            ai_client,
            theme,
        )
        
            presentation_service.initialize()

            self.services.register(
                PresentationService,
                presentation_service,
            )

            # -----------------------------------------
            # Export Service
            # -----------------------------------------

            export_service = ExportService(
                slide_service
            )

            export_service.initialize()

            self.services.register(
                ExportService,
                export_service,
            )

            logger.info(
                "All services initialized."
            )

            # -----------------------------------------
            # Main Window
            # -----------------------------------------

            self.window = MainWindow(self)

            logger.info(
                "MainWindow created."
            )

        except Exception:

            logger.exception(
                "Application initialization failed."
            )

            traceback.print_exc()

            raise

    # -------------------------------------------------

    def run(self):

        self.initialize()

        self.window.show()

        return_code = self.qt.exec()

        self.shutdown()

        return return_code

    # -------------------------------------------------

    def shutdown(self):

        print("APP Shutdown")

        shutdown_order = [

            ExportService,

            PresentationService,

            ProjectService,

            SlideService,

            DatabaseService,
            
            SettingsService,

        ]

        for service_type in shutdown_order:

            if self.services.exists(service_type):

                self.services.get(
                    service_type
                ).shutdown()

        if self.services.exists(LoggerService):

            logger = self.services.get(
                LoggerService
            )

            logger.info(
                "Application closed."
            )

            logger.shutdown()

        self.services.clear()
    
    def register_ai_providers(
    self,
    manager: ProviderManager,
):

        fake = FakeAIProvider()

        fake.initialize()

        manager.register(fake)

        #
        # آینده
        #

        # ollama = OllamaProvider()
        # ollama.initialize()
        # manager.register(ollama)

        # openai = OpenAIProvider(...)
        # openai.initialize()
        # manager.register(openai)
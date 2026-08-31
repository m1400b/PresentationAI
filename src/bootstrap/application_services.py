"""
PresentationAI

Application Services Bootstrap
"""

from __future__ import annotations

from themes.base_theme import (
    BaseTheme,
)

from src.core.service_container import ServiceContainer

from src.database.database_service import (
    DatabaseService,
)

from src.repositories.slide_repository import (
    SlideRepository,
)

from src.repositories.element_repository import (
    ElementRepository,
)

from src.services.slide_service import (
    SlideService,
)

from src.services.layout_engine import (
    LayoutEngine,
)

from src.services.presentation_service import (
    PresentationService,
)

from src.layouts.register_layouts import (
    create_default_layout_registry,
)

from src.ai.ai_client import (
    AIClient,
)

from src.ai.providers.fake_ai_provider import (
    FakeAIProvider,
)

from src.ai.providers.provider_manager import (
    ProviderManager,
)


def create_application_services(
    database_path: str = "database/app.db",
) -> ServiceContainer:
    """
    Creates and wires application services.

    Dependency graph:

        DatabaseService
              |
        +-----+-----+
        |           |
        v           v
    SlideRepo   ElementRepo
        |           |
        +-----+-----+
              |
              v
        SlideService
              |
              v
        PresentationService
    """

    container = ServiceContainer()

    # =================================================
    # Database
    # =================================================

    database = DatabaseService(
        database_path
    )

    container.register(
        DatabaseService,
        database,
    )

    # =================================================
    # Repositories
    # =================================================

    slide_repository = SlideRepository(
        database,
    )

    element_repository = ElementRepository(
        database,
    )

    container.register(
        SlideRepository,
        slide_repository,
    )

    container.register(
        ElementRepository,
        element_repository,
    )

    # =================================================
    # Slide Service
    # =================================================

    slide_service = SlideService(
        slide_repository,
        element_repository,
    )

    container.register(
        SlideService,
        slide_service,
    )

    # =================================================
    # AI
    # =================================================

    provider_manager = ProviderManager()

    provider_manager.register(
        FakeAIProvider()
    )

    ai_client = AIClient(
        provider_manager
    )

    container.register(
        AIClient,
        ai_client,
    )

    # =================================================
    # Layout Engine
    # =================================================

    layout_registry = (
        create_default_layout_registry()
    )

    layout_engine = LayoutEngine(
        layout_registry
    )

    container.register(
        LayoutEngine,
        layout_engine,
    )

    # =================================================
    # Theme
    # =================================================
    
    theme = BaseTheme()
    
    container.register(
        BaseTheme,
        theme,
    )
    
    # =================================================
    # Presentation Service
    # =================================================
    
    presentation_service = PresentationService(
        slide_service,
        layout_engine,
        ai_client,
        theme,
    )
    
    container.register(
        PresentationService,
        presentation_service,
    )
    
    return container
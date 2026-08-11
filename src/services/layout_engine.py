"""
PresentationAI

Layout Engine
"""

from __future__ import annotations

from src.ai.layout_registry import (
    LayoutRegistry,
)

from src.models.presentation import (
    Presentation,
)

from src.models.presentation_plan import (
    PresentationPlan,
)

from themes.base_theme import (
    BaseTheme,
)


class LayoutEngine:
    """
    Converts a PresentationPlan
    into a Presentation.
    """

    # -------------------------------------------------

    def __init__(
        self,
        registry: LayoutRegistry,
    ):

        self._registry = registry

    # -------------------------------------------------

    @property
    def registry(
        self,
    ) -> LayoutRegistry:

        return self._registry

    # -------------------------------------------------

    def build(
        self,
        plan: PresentationPlan,
        theme: BaseTheme,
    ) -> Presentation:
        """
        Builds a Presentation.
        """

        presentation = Presentation()

        presentation.title = plan.title

        presentation.theme = theme.copy()

        for planned_slide in plan.slides:

            slide = self.build_slide(

                planned_slide,

                theme,

            )

            presentation.add_slide(

                slide

            )

        return presentation
        # -------------------------------------------------
    # Slide Builder
    # -------------------------------------------------

    def build_slide(
        self,
        planned_slide,
        theme: BaseTheme,
    ):
        """
        Builds a single slide.
        """

        builder = self._registry.find_builder(

            planned_slide

        )

        return builder.build(

            planned_slide,

            theme,

        )

    # -------------------------------------------------

    def can_build(
        self,
        planned_slide,
    ) -> bool:
        """
        Returns True if a suitable
        builder exists.
        """

        try:

            self._registry.find_builder(

                planned_slide

            )

            return True

        except Exception:

            return False

    # -------------------------------------------------

    def available_layouts(
        self,
    ) -> list[str]:
        """
        Returns all registered layouts.
        """

        return self._registry.names()
    
        # -------------------------------------------------
    # Utilities
    # -------------------------------------------------

    def clear(
        self,
    ) -> None:
        """
        Clears the registry.
        """

        self._registry.clear()

    # -------------------------------------------------

    def reload(
        self,
        registry: LayoutRegistry,
    ) -> None:
        """
        Replaces the current registry.
        """

        self._registry = registry

    # -------------------------------------------------

    def __len__(
        self,
    ) -> int:

        return len(
            self._registry
        )

    # -------------------------------------------------

    def __contains__(
        self,
        layout: str,
    ) -> bool:

        return (

            layout.lower()

            in

            self._registry

        )

    # -------------------------------------------------

    def __repr__(
        self,
    ) -> str:

        return (

            f"<LayoutEngine "

            f"layouts={len(self)}>"

        )
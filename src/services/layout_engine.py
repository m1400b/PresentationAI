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

from src.models.presentation_draft import (
    PresentationDraft,
)

from themes.base_theme import (
    BaseTheme,
)


class LayoutEngine:
    """
    Converts PresentationDraft
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
        draft: PresentationDraft,
        theme: BaseTheme,
    ) -> Presentation:
        """
        Builds final Presentation.
        """

        presentation = Presentation()


        presentation.title = (
            draft.title
        )


        presentation.theme = (
            theme.copy()
        )


        for draft_slide in draft.slides:

            slide = self.build_slide(
                draft_slide,
                theme,
            )

            presentation.add_slide(
                slide
            )


        return presentation


    # -------------------------------------------------
    # Slide
    # -------------------------------------------------

    def build_slide(
        self,
        draft_slide,
        theme: BaseTheme,
    ):
        """
        Builds a single slide.
        """


        builder = (
            self._registry.find_builder(
                draft_slide
            )
        )


        return builder.build(
            draft_slide,
        )


    # -------------------------------------------------

    def can_build(
        self,
        draft_slide,
    ) -> bool:
        """
        Checks if layout exists.
        """

        try:

            self._registry.find_builder(
                draft_slide
            )

            return True


        except Exception:

            return False


    # -------------------------------------------------

    def available_layouts(
        self,
    ) -> list[str]:

        return self._registry.names()


    # -------------------------------------------------

    def clear(
        self,
    ) -> None:

        self._registry.clear()


    # -------------------------------------------------

    def reload(
        self,
        registry: LayoutRegistry,
    ) -> None:

        self._registry = registry


    # -------------------------------------------------

    def __len__(
        self,
    ):

        return len(
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
"""
PresentationAI

Base Layout Builder
"""

from __future__ import annotations

from abc import ABC
from abc import abstractmethod

from src.models.draft_slide import (
    DraftSlide,
)

from src.models.slide import (
    Slide,
)


class BaseLayoutBuilder(ABC):
    """
    Base class for all layout builders.

    Responsibilities
    ----------------
    • Validate DraftSlide
    • Create Slide
    • Allow subclasses to render
    • Perform common post-processing
    """

    # =================================================
    # Layout Information
    # =================================================

    @property
    @abstractmethod
    def layout_name(
        self,
    ) -> str:
        """
        Unique layout identifier.
        """
        ...

    # -------------------------------------------------

    def supports(
        self,
        layout: str,
    ) -> bool:
        """
        Returns True when this builder supports
        the supplied layout name.
        """

        if not layout:
            return False

        return (
            layout.strip().lower()
            ==
            self.layout_name.strip().lower()
        )

    # -------------------------------------------------

    def can_build(
        self,
        planned_slide,
    ) -> bool:
        """
        Returns True when this builder can build
        the supplied planned slide.

        This method exists so LayoutRegistry can
        perform capability-based lookup.

        Subclasses may override this method when
        they need more advanced decision logic.
        """

        if planned_slide is None:
            return False

        layout = getattr(
            planned_slide,
            "layout",
            "",
        )

        if not layout:
            return False

        return self.supports(
            layout
        )

    # =================================================
    # Build Pipeline
    # =================================================

    def build(
        self,
        draft: DraftSlide,
    ) -> Slide:
        """
        Template Method.

        Final algorithm executed for every
        layout builder.
        """

        self.validate(
            draft
        )

        slide = self.create_slide(
            draft
        )

        self.render(
            slide,
            draft,
        )

        self.post_process(
            slide
        )

        return slide

    # -------------------------------------------------

    def create_slide(
        self,
        draft: DraftSlide,
    ) -> Slide:
        """
        Creates an empty Slide instance.
        """

        slide = Slide()

        slide.order = draft.order

        slide.layout = draft.layout

        slide.title = draft.title

        slide.subtitle = draft.subtitle

        slide.bullets = list(
            draft.bullets
        )

        slide.notes = draft.notes

        slide.transition = draft.transition

        slide.animation = draft.animation

        return slide

    # =================================================
    # Rendering
    # =================================================

    @abstractmethod
    def render(
        self,
        slide: Slide,
        draft: DraftSlide,
    ) -> None:
        """
        Subclasses create elements here.
        """
        ...

    # =================================================
    # Validation
    # =================================================

    def validate(
        self,
        draft: DraftSlide,
    ) -> None:
        """
        Validates required slide data.
        """

        if draft is None:

            raise ValueError(
                "DraftSlide cannot be None."
            )

        if not draft.title.strip():

            raise ValueError(
                "Slide title cannot be empty."
            )

    # =================================================
    # Post Processing
    # =================================================

    def post_process(
        self,
        slide: Slide,
    ) -> None:
        """
        Final processing after rendering.

        Subclasses may override.
        """

        self.apply_defaults(
            slide
        )

    # -------------------------------------------------

    def apply_defaults(
        self,
        slide: Slide,
    ) -> None:
        """
        Applies default properties.
        """

        if slide.background is None:

            slide.background = "default"

    # =================================================
    # Metadata
    # =================================================

    def copy_metadata(
        self,
        slide: Slide,
        draft: DraftSlide,
    ) -> None:
        """
        Copies metadata from DraftSlide
        into Slide.
        """

        slide.notes = draft.notes

        # These attributes are not currently
        # declared in Slide, so only assign them
        # when the model supports them.

        if hasattr(
            slide,
            "summary",
        ):

            slide.summary = draft.summary

        if hasattr(
            slide,
            "keywords",
        ):

            slide.keywords = list(
                draft.keywords
            )

        if hasattr(
            slide,
            "references",
        ):

            slide.references = list(
                draft.references
            )

    # =================================================
    # Element Factories
    # =================================================

    def create_text_element(
        self,
        text: str,
        role: str,
    ):
        """
        Creates a text element placeholder.

        Position and style are assigned later.
        """

        return {
            "type": "text",
            "role": role,
            "text": text,
        }

    # -------------------------------------------------

    def create_image_element(
        self,
        prompt: str,
    ):
        """
        Creates an image placeholder.
        """

        return {
            "type": "image",
            "prompt": prompt,
        }

    # -------------------------------------------------

    def create_chart_element(
        self,
        chart_type: str = "auto",
    ):
        """
        Creates a chart placeholder.
        """

        return {
            "type": "chart",
            "chart_type": chart_type,
        }

    # -------------------------------------------------

    def create_table_element(
        self,
    ):
        """
        Creates a table placeholder.
        """

        return {
            "type": "table",
        }

    # =================================================
    # Representation
    # =================================================

    def __repr__(
        self,
    ) -> str:

        return (
            f"<{self.__class__.__name__} "
            f"layout='{self.layout_name}'>"
        )


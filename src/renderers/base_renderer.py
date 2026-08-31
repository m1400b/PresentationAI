"""
PresentationAI

Base Renderer
"""

from __future__ import annotations

from abc import ABC
from abc import abstractmethod

from pathlib import Path
from src.models.presentation import Presentation


class BaseRenderer(ABC):
    """
    Base class for all renderers.

    Responsibilities
    ----------------
    • Validate Presentation
    • Convert Presentation to output format
    • Provide common renderer contract
    """


    # =================================================
    # Identity
    # =================================================

    @property
    @abstractmethod
    def renderer_name(
        self,
    ) -> str:
        """
        Unique renderer name.
        """
        ...


    # =================================================
    # Main Render
    # =================================================

    @abstractmethod
    def render(
        self,
        presentation: Presentation,
        output_path: str,
    ) -> str:
        """
        Converts Presentation into output file.

        Returns:
            Generated file path
        """
        ...


    # =================================================
    # Validation
    # =================================================

    def validate(
    self,
    presentation,
):

        if presentation is None:
            raise ValueError(
                "Presentation cannot be None."
            )
    
        if not isinstance(
            presentation,
            Presentation,
        ):
            raise TypeError(
                "Invalid presentation type."
            )
    
        if not presentation.slides:
            raise ValueError(
                "Presentation has no slides."
            )

    # =================================================
    # Helpers
    # =================================================

    def ensure_output(
    self,
    output_path:str,
)->str:

        path = Path(output_path)

        path.parent.mkdir(
            parents=True,
            exist_ok=True
        )

        return str(
            path.resolve()
        )


    # =================================================
    # Representation
    # =================================================

    def __repr__(
        self,
    ) -> str:

        return (
            f"<{self.__class__.__name__} "
            f"name='{self.renderer_name}'>"
        )
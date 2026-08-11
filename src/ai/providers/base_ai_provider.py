"""
PresentationAI

Base AI Provider
"""

from __future__ import annotations

from abc import ABC
from abc import abstractmethod

from src.ai.prompt_request import (
    PromptRequest,
)


class BaseAIProvider(ABC):
    """
    Base class for every AI provider.

    Examples:

        - Fake
        - Ollama
        - LM Studio
        - OpenAI
        - Gemini
        - Claude
        - DeepSeek
    """

    # -------------------------------------------------
    # Information
    # -------------------------------------------------

    @property
    @abstractmethod
    def name(self) -> str:
        """
        Provider display name.
        """
        ...

    # -------------------------------------------------

    @property
    @abstractmethod
    def is_local(self) -> bool:
        """
        True for local providers.
        """
        ...

    # -------------------------------------------------

    @property
    def is_online(self) -> bool:
        """
        True for online providers.
        """

        return not self.is_local

    # -------------------------------------------------
    # Lifecycle
    # -------------------------------------------------

    def initialize(self) -> None:
        """
        Optional initialization.
        """

        pass

    # -------------------------------------------------

    def shutdown(self) -> None:
        """
        Optional cleanup.
        """

        pass

    # -------------------------------------------------
    # Availability
    # -------------------------------------------------

    @abstractmethod
    def available(self) -> bool:
        """
        Returns True if provider
        can currently be used.
        """
        ...

    # -------------------------------------------------
    # Models
    # -------------------------------------------------

    def models(self) -> list[str]:
        """
        Returns available models.

        Override if provider supports it.
        """

        return []

    # -------------------------------------------------

    def set_model(
        self,
        model: str,
    ) -> None:
        """
        Select active model.

        Override if supported.
        """

        pass

    # -------------------------------------------------
    # Generation
    # -------------------------------------------------

    @abstractmethod
    def generate(
        self,
        request: PromptRequest,
    ) -> str:
        """
        Generate presentation JSON.

        Parameters
        ----------
        request:
            Presentation generation request.

        Returns
        -------
        str
            JSON string containing presentation data.
        """

        ...

    # -------------------------------------------------
    # Representation
    # -------------------------------------------------

    def __str__(self) -> str:

        return self.name

    # -------------------------------------------------

    def __repr__(self) -> str:

        return (
            f"<{self.__class__.__name__} "
            f"name='{self.name}' "
            f"local={self.is_local}>"
        )
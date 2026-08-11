"""
PresentationAI

AI Client
"""

from __future__ import annotations

from src.ai.prompt_builder import (
    PromptBuilder,
    PromptRequest,
)
from src.ai.prompt_builder import (
    PromptBuilder,
    PromptRequest,
)

from src.ai.providers.provider_manager import (
    ProviderManager,
)


class AIClient:
    """
    High-level AI gateway.

    Responsibilities
    ----------------
    - Build prompt
    - Select provider
    - Call AI provider

    It does NOT parse JSON.
    """

    # -------------------------------------------------

    def __init__(
        self,
        provider_manager: ProviderManager,
    ):

        self.providers = provider_manager

        self.prompt_builder = PromptBuilder()

    # -------------------------------------------------

    @property
    def current_provider(self):

        return self.providers.current

    # -------------------------------------------------

    def generate(
        self,
        request: PromptRequest,
    ) -> str:

        bundle = self.prompt_builder.build(
            request
        )

        provider = self.providers.best_provider(
    request
)

        return provider.generate(
            bundle
        )

    # -------------------------------------------------

    def generate_with(
        self,
        provider_name: str,
        request: PromptRequest,
    ) -> str:
    
        bundle = self.prompt_builder.build(
            request
        )
    
        provider = self.providers.provider(
            provider_name
        )
    
        return provider.generate(
            bundle
        )
    # -------------------------------------------------

    def available_providers(self):

        return self.providers.names()

    # -------------------------------------------------

    def set_provider(
        self,
        name: str,
    ):

        self.providers.set_current(name)

    # -------------------------------------------------

    def __repr__(self):

        return (
            f"<AIClient "
            f"provider={self.current_provider.name}>"
        )
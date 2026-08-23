"""
PresentationAI

Provider Manager
"""

from __future__ import annotations

from src.ai.prompt_request import PromptRequest
from src.ai.providers.base_ai_provider import BaseAIProvider


class ProviderManager:
    """
    Registers AI providers and selects
    the best provider for a request.
    """

    # -------------------------------------------------

    def __init__(self):

        self._providers: dict[
            str,
            BaseAIProvider,
        ] = {}

        self._current: str | None = None

    # -------------------------------------------------
    # Registration
    # -------------------------------------------------

    def register(
        self,
        provider: BaseAIProvider,
    ) -> None:

        name = provider.name.lower()

        self._providers[name] = provider

        if self._current is None:

            self._current = name

    # -------------------------------------------------

    def unregister(
        self,
        name: str,
    ) -> None:

        name = name.lower()

        self._providers.pop(
            name,
            None,
        )

        if self._current == name:

            self._current = None

    # -------------------------------------------------
    # Lookup
    # -------------------------------------------------

    def provider(
        self,
        name: str,
    ) -> BaseAIProvider:

        return self._providers[
            name.lower()
        ]

    # -------------------------------------------------

    def has_provider(
        self,
        name: str,
    ) -> bool:

        return (
            name.lower()
            in self._providers
        )

    # -------------------------------------------------

    @property
    def current(
        self,
    ) -> BaseAIProvider:

        if self._current is None:

            raise RuntimeError(
                "No provider selected."
            )

        return self.provider(
            self._current
        )

    # -------------------------------------------------

    def set_current(
        self,
        name: str,
    ) -> None:

        name = name.lower()

        if name not in self._providers:

            raise ValueError(
                f"Unknown provider: {name}"
            )

        self._current = name

    # -------------------------------------------------
    # Lists
    # -------------------------------------------------

    def names(self) -> list[str]:

        return sorted(

            provider.name

            for provider

            in self._providers.values()

        )

    # -------------------------------------------------

    def local_providers(
        self,
    ) -> list[BaseAIProvider]:

        return [

            provider

            for provider

            in self._providers.values()

            if provider.is_local

        ]

    # -------------------------------------------------

    def online_providers(
        self,
    ) -> list[BaseAIProvider]:

        return [

            provider

            for provider

            in self._providers.values()

            if provider.is_online

        ]

    # -------------------------------------------------

    def available_providers(
        self,
    ) -> list[BaseAIProvider]:

        providers = []

        for provider in self._providers.values():

            try:

                if provider.available():

                    providers.append(
                        provider
                    )

            except Exception:

                pass

        return providers

    # -------------------------------------------------
    # Auto Selection
    # -------------------------------------------------

    def best_provider(
        self,
        request: PromptRequest,
    ) -> BaseAIProvider:

        #
        # User selected a provider
        #

        if (

            request.provider

            and

            request.provider.lower()

            != "auto"

        ):

            return self.provider(

                request.provider

            )

        #
        # Offline only
        #

        if request.offline_only:

            for provider in self.local_providers():

                if provider.available():

                    return provider

        #
        # Online allowed
        #

        if request.allow_online:

            for provider in self.online_providers():

                if provider.available():

                    return provider

        #
        # Local fallback
        #

        for provider in self.local_providers():

            if provider.available():

                return provider

        #
        # Last fallback
        #

        if self.has_provider("fake"):

            return self.provider("fake")

        raise RuntimeError(

            "No AI provider available."

        )

    # -------------------------------------------------

    def clear(self):

        self._providers.clear()

        self._current = None

    # -------------------------------------------------

    def __len__(self):

        return len(

            self._providers

        )

    # -------------------------------------------------

    def __contains__(
        self,
        name: str,
    ):

        return (

            name.lower()

            in self._providers

        )

    # -------------------------------------------------

    def __repr__(self):

        return (

            f"<ProviderManager "

            f"providers={len(self)} "

            f"current={self._current}>"

        )
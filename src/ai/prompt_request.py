"""
PresentationAI

Prompt Request
"""

from __future__ import annotations

from dataclasses import (
    dataclass,
    field,
)


@dataclass(slots=True)
class PromptRequest:
    """
    Represents an AI prompt request.
    """

    topic: str

    language: str = "en"

    provider: str = "auto"

    slide_count: int = 10

    offline_only: bool = False

    allow_online: bool = True

    theme: str = "corporate"

    audience: str = ""

    notes: str = ""

    metadata: dict[
        str,
        object,
    ] = field(
        default_factory=dict,
    )
        # -------------------------------------------------
    # Properties
    # -------------------------------------------------

    @property
    def is_auto_provider(
        self,
    ) -> bool:
        """
        Returns True if provider
        selection is automatic.
        """

        return (

            self.provider.lower()

            == "auto"

        )

    # -------------------------------------------------

    @property
    def online_enabled(
        self,
    ) -> bool:
        """
        Returns True if online
        providers may be used.
        """

        return (

            self.allow_online

            and

            not self.offline_only

        )

    # -------------------------------------------------

    @property
    def has_notes(
        self,
    ) -> bool:
        """
        Returns True if notes exist.
        """

        return bool(

            self.notes.strip()

        )

    # -------------------------------------------------

    @property
    def has_audience(
        self,
    ) -> bool:
        """
        Returns True if audience exists.
        """

        return bool(

            self.audience.strip()

        )

    # -------------------------------------------------

    def copy(
        self,
    ) -> "PromptRequest":
        """
        Returns a copy of the request.
        """

        from copy import deepcopy

        return deepcopy(
            self
        )
    
        # -------------------------------------------------

    def __post_init__(
        self,
    ) -> None:
        """
        Normalizes request values.
        """

        self.topic = self.topic.strip()

        self.language = (
            self.language.strip().lower()
        )

        self.provider = (
            self.provider.strip().lower()
        )

        self.theme = (
            self.theme.strip().lower()
        )

        self.audience = (
            self.audience.strip()
        )

        self.notes = (
            self.notes.strip()
        )

        if self.slide_count < 1:

            self.slide_count = 1

    # -------------------------------------------------

    def __repr__(
        self,
    ) -> str:

        return (

            f"<PromptRequest "

            f"topic='{self.topic}' "

            f"provider='{self.provider}' "

            f"slides={self.slide_count}>"

        )
    
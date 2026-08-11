"""
PresentationAI

Layout Registry
"""

from __future__ import annotations

from src.layouts.base_layout_builder import (
    BaseLayoutBuilder,
)

from src.models.planned_slide import (
    PlannedSlide,
)


# =================================================
# Layout Normalization
# =================================================

def normalize_layout(
    layout: str,
) -> str:
    """
    Normalizes layout names into the canonical
    layout identifiers used by PresentationAI.

    This function is intentionally independent
    from registered builders so the application
    can safely start with zero builders.
    """

    if not layout:
        return "title_content"

    value = str(layout).strip().lower()

    # ---------------------------------------------
    # Remove common separators
    # ---------------------------------------------

    normalized = (
        value
        .replace("_", " ")
        .replace("-", " ")
        .replace("+", " ")
    )

    normalized = " ".join(
        normalized.split()
    )

    # ---------------------------------------------
    # Aliases
    # ---------------------------------------------

    aliases = {

        # Title
        "title": "title_slide",
        "title slide": "title_slide",
        "titleslide": "title_slide",

        # Title + Content
        "content": "title_content",
        "title content": "title_content",
        "title and content": "title_content",
        "title content slide": "title_content",
        "titlecontent": "title_content",

        # Two columns
        "two column": "two_columns",
        "two columns": "two_columns",
        "2 column": "two_columns",
        "2 columns": "two_columns",
        "two column slide": "two_columns",
        "twocolumns": "two_columns",

        # Comparison
        "compare": "comparison",
        "comparison slide": "comparison",

        # Timeline
        "timeline slide": "timeline",

        # Gallery
        "gallery slide": "gallery",

        # Image
        "image": "image",
        "image slide": "image",

        # Chart
        "chart": "chart",
        "chart slide": "chart",

        # Table
        "table": "table",
        "table slide": "table",

        # Process
        "process": "process",
        "process slide": "process",

        # Quote
        "quote": "quote",
        "quote slide": "quote",

        # Statistics
        "statistics": "statistics",
        "statistic": "statistics",
        "statistics slide": "statistics",

        # Conclusion
        "conclusion": "conclusion",
        "conclusion slide": "conclusion",

        # Agenda
        "agenda": "agenda",
        "agenda slide": "agenda",

    }

    return aliases.get(
        normalized,
        normalized.replace(" ", "_"),
    )


# =================================================
# Layout Registry
# =================================================

class LayoutRegistry:
    """
    Registers and resolves layout builders.

    The registry is intentionally safe to use with
    zero registered builders.
    """

    # -------------------------------------------------

    def __init__(
        self,
    ) -> None:

        self._builders: dict[
            str,
            BaseLayoutBuilder,
        ] = {}

    # =================================================
    # Registration
    # =================================================

    def register(
        self,
        builder: BaseLayoutBuilder,
    ) -> None:
        """
        Registers a layout builder.
        """

        if builder is None:

            raise ValueError(
                "Builder cannot be None."
            )

        layout = normalize_layout(
            builder.layout_name
        )

        self._builders[
            layout
        ] = builder

    # -------------------------------------------------

    def unregister(
        self,
        layout: str,
    ) -> None:
        """
        Removes a builder.
        """

        normalized = normalize_layout(
            layout
        )

        self._builders.pop(
            normalized,
            None,
        )

    # =================================================
    # Lookup
    # =================================================

    def has_builder(
        self,
        layout: str,
    ) -> bool:
        """
        Returns True if a builder exists.
        """

        normalized = normalize_layout(
            layout
        )

        return normalized in self._builders

    # -------------------------------------------------

    def builder(
        self,
        layout: str,
    ) -> BaseLayoutBuilder:
        """
        Returns a builder by layout name.
        """

        normalized = normalize_layout(
            layout
        )

        try:

            return self._builders[
                normalized
            ]

        except KeyError as exc:

            raise ValueError(
                f"Unknown layout: {layout}"
            ) from exc

    # -------------------------------------------------

    def find_builder(
        self,
        planned: PlannedSlide,
    ) -> BaseLayoutBuilder:
        """
        Finds a builder for a PlannedSlide.

        Fast lookup is attempted first.
        If no exact builder exists, all
        registered builders are checked.
        """

        if planned is None:

            raise ValueError(
                "PlannedSlide cannot be None."
            )

        layout = normalize_layout(
            planned.layout
        )

        # -----------------------------------------
        # Fast lookup
        # -----------------------------------------

        if layout in self._builders:

            return self._builders[
                layout
            ]

        # -----------------------------------------
        # Capability lookup
        # -----------------------------------------

        for builder in self._builders.values():

            if builder.can_build(
                planned
            ):

                return builder

            if builder.supports(
                planned.layout
            ):

                return builder

        raise RuntimeError(
            f"No builder found for "
            f"layout '{planned.layout}'."
        )

    # =================================================
    # Collection
    # =================================================

    def builders(
        self,
    ) -> list[BaseLayoutBuilder]:
        """
        Returns all registered builders.
        """

        return list(
            self._builders.values()
        )

    # -------------------------------------------------

    def names(
        self,
    ) -> list[str]:
        """
        Returns registered layout names.
        """

        return sorted(
            self._builders.keys()
        )

    # -------------------------------------------------

    def clear(
        self,
    ) -> None:
        """
        Removes all registered builders.
        """

        self._builders.clear()

    # =================================================
    # Utilities
    # =================================================

    def __len__(
        self,
    ) -> int:

        return len(
            self._builders
        )

    # -------------------------------------------------

    def __contains__(
        self,
        layout: str,
    ) -> bool:

        return normalize_layout(
            layout
        ) in self._builders

    # -------------------------------------------------

    def __iter__(
        self,
    ):

        return iter(
            self._builders.values()
        )

    # -------------------------------------------------

    def __repr__(
        self,
    ) -> str:

        return (
            f"<LayoutRegistry "
            f"builders={len(self)}>"
        )
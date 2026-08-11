"""
PresentationAI

Theme Manager
"""

from __future__ import annotations

from themes.base_theme import (
    BaseTheme,
)


class ThemeManager:
    """
    Registers and manages
    presentation themes.
    """

    # -------------------------------------------------

    def __init__(self):

        self._themes: dict[
            str,
            BaseTheme,
        ] = {}

        self._current: str | None = None

    # -------------------------------------------------
    # Registration
    # -------------------------------------------------

    def register(
        self,
        theme: BaseTheme,
    ) -> None:
        """
        Registers a theme.
        """

        name = theme.name.lower()

        self._themes[name] = theme

        if self._current is None:

            self._current = name

    # -------------------------------------------------

    def unregister(
        self,
        name: str,
    ) -> None:
        """
        Removes a theme.
        """

        name = name.lower()

        self._themes.pop(
            name,
            None,
        )

        if self._current == name:

            self._current = None
        # -------------------------------------------------
    # Lookup
    # -------------------------------------------------

    def theme(
        self,
        name: str,
    ) -> BaseTheme:
        """
        Returns a theme by name.
        """

        return self._themes[
            name.lower()
        ]

    # -------------------------------------------------

    def has_theme(
        self,
        name: str,
    ) -> bool:
        """
        Returns True if theme exists.
        """

        return (

            name.lower()

            in self._themes

        )

    # -------------------------------------------------

    @property
    def current(
        self,
    ) -> BaseTheme:
        """
        Returns current theme.
        """

        if self._current is None:

            raise RuntimeError(
                "No theme selected."
            )

        return self.theme(
            self._current
        )

    # -------------------------------------------------

    def set_current(
        self,
        name: str,
    ) -> None:
        """
        Sets current theme.
        """

        name = name.lower()

        if name not in self._themes:

            raise ValueError(

                f"Unknown theme: {name}"

            )

        self._current = name

    # -------------------------------------------------

    @property
    def current_name(
        self,
    ) -> str | None:

        return self._current

    # -------------------------------------------------

    def names(
        self,
    ) -> list[str]:
        """
        Returns registered theme names.
        """

        return sorted(

            theme.name

            for theme

            in self._themes.values()

        )
    
        # -------------------------------------------------
    # Utilities
    # -------------------------------------------------

    def copy_current(
        self,
    ) -> BaseTheme:
        """
        Returns a copy of the current theme.
        """

        return self.current.copy()

    # -------------------------------------------------

    def clear(
        self,
    ) -> None:
        """
        Removes all registered themes.
        """

        self._themes.clear()

        self._current = None

    # -------------------------------------------------

    def __len__(
        self,
    ) -> int:

        return len(
            self._themes
        )

    # -------------------------------------------------

    def __contains__(
        self,
        name: str,
    ) -> bool:

        return (

            name.lower()

            in self._themes

        )

    # -------------------------------------------------

    def __iter__(
        self,
    ):

        return iter(

            self._themes.values()

        )

    # -------------------------------------------------

    def __repr__(
        self,
    ) -> str:

        return (

            f"<ThemeManager "

            f"themes={len(self)} "

            f"current={self._current}>"

        )
    
    def all(
    self,
    ) -> list[BaseTheme]:
        """
        Returns all registered themes.
        """
    
        return list(
            self._themes.values()
        )
    
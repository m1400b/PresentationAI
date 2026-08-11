"""
PresentationAI

Clipboard Service
"""

from __future__ import annotations

from copy import deepcopy
import uuid

from src.core.service import BaseService

from src.models.elements.element import Element


class ClipboardService(BaseService):
    """
    Internal clipboard for slide elements.

    Stores a copy of the last copied element.
    """

    # -------------------------------------------------

    def __init__(self):

        self._element: Element | None = None

    # -------------------------------------------------

    def initialize(self):

        print("ClipboardService.initialize()")

    # -------------------------------------------------

    def shutdown(self):

        print("ClipboardService.shutdown()")

        self.clear()

    # -------------------------------------------------
    # State
    # -------------------------------------------------

    def clear(self):

        self._element = None

    # -------------------------------------------------

    def is_empty(self) -> bool:

        return self._element is None

    # -------------------------------------------------

    def has_data(self) -> bool:

        return self._element is not None

    # -------------------------------------------------
    # Copy / Cut
    # -------------------------------------------------

    def copy(
        self,
        element: Element,
    ):

        if element is None:

            return

        self._element = deepcopy(element)

    # -------------------------------------------------

    def cut(
        self,
        element: Element,
    ):

        #
        # Same as copy.
        # Caller removes the element
        # from the slide.
        #

        self.copy(element)
        # -------------------------------------------------
    # Paste
    # -------------------------------------------------

    def paste(
        self,
        offset: float = 20,
    ) -> Element | None:
        """
        Creates a new independent copy of the
        clipboard element.
        """

        if self._element is None:

            return None

        element = deepcopy(self._element)

        #
        # New identity
        #

        element.id = str(uuid.uuid4())

        #
        # Do not keep selected state
        #

        element.selected = False

        #
        # Offset position
        #

        element.move_by(
            offset,
            offset,
        )

        return element

    # -------------------------------------------------

    def peek(self) -> Element | None:
        """
        Returns a copy of the clipboard contents
        without modifying the clipboard.
        """

        if self._element is None:

            return None

        return deepcopy(self._element)

    # -------------------------------------------------

    def __repr__(self):

        if self.is_empty():

            return "<ClipboardService empty>"

        return (
            f"<ClipboardService "
            f"type={self._element.type}>"
        )
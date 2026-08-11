"""
PresentationAI

Selection Manager
"""

from __future__ import annotations

from PySide6.QtCore import QObject, Signal

from src.models.slide import Slide
from src.models.elements.element import Element

class SelectionManager(QObject):
    """
    Manages current editor selection.

    Only one slide and one element are selected
    in v1.

    Multi-selection will be added later without
    changing the public API.
    """
    selection_changed = Signal()
    # -------------------------------------------------

    def __init__(self):
        
        super().__init__()
        self._slide: Slide | None = None

        self._element: Element | None = None

    # -------------------------------------------------
    # Slide
    # -------------------------------------------------

    @property
    def current_slide(self) -> Slide | None:

        return self._slide

    # -------------------------------------------------

    def set_slide(
        self,
        slide: Slide | None,
    ):

        if self._slide is slide:

            return

        self._slide = slide

        self._element = None

        self.selection_changed.emit()
    # -------------------------------------------------

    def has_slide(self) -> bool:

        return self._slide is not None

    # -------------------------------------------------
    # Element
    # -------------------------------------------------

    @property
    def current_element(self) -> Element | None:

        return self._element

    # -------------------------------------------------

    def set_element(
    self,
    element: Element | None,
):

        if self._element is element:

            return

        self._element = element

        self.selection_changed.emit()

    # -------------------------------------------------

    def has_element(self) -> bool:

        return self._element is not None
        # -------------------------------------------------

    def clear_element(self):

        self._element = None
        self.selection_changed.emit()

    # -------------------------------------------------

    def clear_slide(self):

        self._slide = None

        self._element = None

        self.selection_changed.emit()

    # -------------------------------------------------

    def clear(self):

        self._slide = None

        self._element = None
        self.selection_changed.emit()

    # -------------------------------------------------

    def is_selected(
        self,
        element: Element,
    ) -> bool:

        return self._element is element

    # -------------------------------------------------

    def select_first(self):

        if self._slide is None:

            self._element = None

            self.selection_changed.emit()

            return None

        if not self._slide.elements:

            self._element = None

            self.selection_changed.emit()

            return None

        self._element = self._slide.elements[0]

        self.selection_changed.emit()

        return self._element
    # -------------------------------------------------

    def __repr__(self):

        slide = "None"

        element = "None"

        if self._slide is not None:

            slide = self._slide.title

        if self._element is not None:

            element = self._element.type

        return (

            f"<SelectionManager "

            f"slide={slide!r} "

            f"element={element!r}>"

        )
        
    @property
    def has_selection(self) -> bool:

        return self._element is not None
    
    @property
    def selection_empty(self) -> bool:

        return self._element is None
    
    def selected_element(self) -> Element | None:

        return self._element
    
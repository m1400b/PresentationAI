"""
PresentationAI

Geometry Property Widget
"""

from __future__ import annotations

from PySide6.QtWidgets import (
    QWidget,
    QFormLayout,
    QDoubleSpinBox,
    QGroupBox,
    QVBoxLayout,
)

from src.models.elements.element import Element
from src.services.element_service import ElementService
from src.services.slide_service import SlideService


class GeometryWidget(QWidget):
    """
    Edits geometry of selected element.
    """

    # -------------------------------------------------

    def __init__(self, app):

        super().__init__()

        self.app = app

        self.selection = app.selection

        self.element_service = app.services.get(
            ElementService
        )

        self.slide_service = app.services.get(
            SlideService
        )

        self._loading = False

        self.build_ui()

    # -------------------------------------------------

    def build_ui(self):

        layout = QVBoxLayout(self)

        group = QGroupBox("Geometry")

        form = QFormLayout(group)

        #
        # X
        #

        self.x_spin = self._create_spinbox()

        form.addRow(
            "X",
            self.x_spin,
        )

        #
        # Y
        #

        self.y_spin = self._create_spinbox()

        form.addRow(
            "Y",
            self.y_spin,
        )

        #
        # Width
        #

        self.width_spin = self._create_spinbox()

        form.addRow(
            "Width",
            self.width_spin,
        )

        #
        # Height
        #

        self.height_spin = self._create_spinbox()

        form.addRow(
            "Height",
            self.height_spin,
        )

        #
        # Rotation
        #

        self.rotation_spin = self._create_spinbox()

        self.rotation_spin.setRange(
            -360,
            360,
        )

        form.addRow(
            "Rotation",
            self.rotation_spin,
        )

        layout.addWidget(group)

        layout.addStretch()

        self._connect_signals()
    
        # -------------------------------------------------

    def _create_spinbox(self):

        spin = QDoubleSpinBox()

        spin.setDecimals(1)

        spin.setRange(
            -10000,
            10000,
        )

        spin.setSingleStep(1)

        return spin

    # -------------------------------------------------

    def _connect_signals(self):

        self.x_spin.editingFinished.connect(
            self._apply_changes
        )

        self.y_spin.editingFinished.connect(
            self._apply_changes
        )

        self.width_spin.editingFinished.connect(
            self._apply_changes
        )

        self.height_spin.editingFinished.connect(
            self._apply_changes
        )

        self.rotation_spin.editingFinished.connect(
            self._apply_changes
        )

    # -------------------------------------------------

    def load(
        self,
        element: Element,
    ):

        self._loading = True

        self.x_spin.setValue(
            element.x
        )

        self.y_spin.setValue(
            element.y
        )

        self.width_spin.setValue(
            element.width
        )

        self.height_spin.setValue(
            element.height
        )

        self.rotation_spin.setValue(
            element.rotation
        )

        self.setEnabled(True)

        self._loading = False

    # -------------------------------------------------

    def clear(self):

        self._loading = True

        self.x_spin.setValue(0)

        self.y_spin.setValue(0)

        self.width_spin.setValue(0)

        self.height_spin.setValue(0)

        self.rotation_spin.setValue(0)

        self.setEnabled(False)

        self._loading = False
    
        # -------------------------------------------------

    def _apply_changes(self):

        if self._loading:
        
            return
    
        element = self.selection.current_element
    
        if element is None:
        
            return
    
        #
        # Move
        #
    
        self.element_service.move(
        
            element,
    
            self.x_spin.value(),
    
            self.y_spin.value(),
    
        )
    
        #
        # Resize
        #
    
        self.element_service.resize(
        
            element,
    
            self.width_spin.value(),
    
            self.height_spin.value(),
    
        )
    
        #
        # Rotate
        #
    
        self.element_service.rotate(
        
            element,
    
            self.rotation_spin.value(),
    
        )
    
        #
        # Save
        #
    
        slide = self.selection.current_slide
    
        if slide is not None:
        
            self.slide_service.save_slide(
                slide
            )
    
        #
        # Refresh UI
        #
    
        self.selection.selection_changed.emit()
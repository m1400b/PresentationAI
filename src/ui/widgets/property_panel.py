"""
PresentationAI

Property Panel
"""

from __future__ import annotations

from PySide6.QtWidgets import (
    QWidget,
    QLabel,
    QVBoxLayout,
    QStackedWidget,
)

from src.models.elements.text_element import TextElement
from src.models.elements.image_element import ImageElement
from src.models.elements.chart_element import ChartElement

from src.ui.widgets.geometry_widget import GeometryWidget
from src.ui.widgets.text_widget import TextWidget
from src.ui.widgets.image_widget import ImageWidget
from src.ui.widgets.chart_widget import ChartWidget


class PropertyPanel(QWidget):
    """
    Displays editable properties of the
    currently selected element.

    The panel listens to SelectionManager and
    automatically switches between property pages.
    """

    # -------------------------------------------------

    def __init__(self, app):

        super().__init__()
        self.slide = None

        self.app = app

        self.selection = app.selection

        self.build_ui()

        self.selection.selection_changed.connect(
            self.refresh
        )

        self.refresh()

    # -------------------------------------------------
    def set_slide(
        self,
        slide,
    ):

        self.slide = slide

        self.refresh()


    def build_ui(self):

        layout = QVBoxLayout(self)

        layout.setContentsMargins(
            8,
            8,
            8,
            8,
        )

        layout.setSpacing(8)

        title = QLabel("Properties")

        title.setStyleSheet(
            """
            font-size:18px;
            font-weight:bold;
            """
        )

        layout.addWidget(title)

        #
        # Empty message
        #

        self.empty_label = QLabel(
            "No element selected."
        )

        self.empty_label.setWordWrap(True)

        layout.addWidget(self.empty_label)

        #
        # Pages
        #

        #
        # Geometry
        #

        self.geometry = GeometryWidget(
            self.app
        )

        layout.addWidget(
            self.geometry
        )

        #
        # Dynamic Pages
        #

        self.pages = QStackedWidget()

        layout.addWidget(
            self.pages,
            1,
        )

        self.build_pages()    
    # -------------------------------------------------

    def build_pages(self):

        self.text_page = TextWidget(
            self.app
        )

        self.image_page = ImageWidget(
            self.app
        )

        self.chart_page = ChartWidget(
            self.app
        )

        self.pages.addWidget(
            self.text_page
        )

        self.pages.addWidget(
            self.image_page
        )

        self.pages.addWidget(
            self.chart_page
        )
    # -------------------------------------------------

    def refresh(self):

        #
        # No slide
        #
    
        if self.slide is None:
        
            self.geometry.hide()
    
            self.pages.hide()
    
            self.empty_label.setText(
                "No slide selected."
            )
    
            self.empty_label.show()
    
            return
    
        element = self.selection.current_element
    
        #
        # No element
        #
    
        if element is None:
        
            self.geometry.hide()
    
            self.pages.hide()
    
            self.empty_label.setText(
                "No element selected."
            )
    
            self.empty_label.show()
    
            return
    
        self.empty_label.hide()
    
        self.geometry.show()
    
        self.pages.show()
    
        self.geometry.load(element)

        #
        # Nothing selected
        #

        if element is None:

            self.empty_label.show()

            self.pages.hide()

            return

        self.empty_label.hide()

        self.pages.show()

        #
        # Text
        #

        if isinstance(
            element,
            TextElement,
        ):

            self.pages.setCurrentWidget(
                self.text_page
            )

            self.text_page.load(
                element
            )

            self.pages.setCurrentWidget(
                self.text_page
            )

            return

        #
        # Image
        #

        if isinstance(
            element,
            ImageElement,
        ):


            self.geometry.load(element)
            
            self.pages.setCurrentWidget(
                            self.image_page
                        )

            self.image_page.load(
                element
            )

            return

        #
        # Chart
        #

        if isinstance(
            element,
            ChartElement,
        ):

            self.geometry.load(element)
            
            self.pages.setCurrentWidget(
                            self.chart_page
                        )


            self.chart_page.load(
                element
            )

            return
    
        # -------------------------------------------------

    def current_element(self):

        """
        Returns currently selected element.
        """

        return self.selection.current_element

    # -------------------------------------------------

    def clear(self):

        """
        Clears current property page.
        """

        self.empty_label.show()

        self.pages.hide()

    # -------------------------------------------------

    def reload(self):

        """
        Reload current page.

        Used after Undo/Redo,
        Clipboard,
        AI modifications,
        etc.
        """

        self.refresh()

    # -------------------------------------------------

    def update_values(self):

        """
        Refresh values without
        rebuilding widgets.

        Will be used while dragging,
        resizing and rotating.
        """

        self.refresh()

    # -------------------------------------------------

    def __repr__(self):

        element = self.selection.current_element

        if element is None:

            return "<PropertyPanel empty>"

        return (
            f"<PropertyPanel "
            f"{element.type}>"
        )
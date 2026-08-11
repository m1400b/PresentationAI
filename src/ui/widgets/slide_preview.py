"""
PresentationAI

Slide Preview Widget
"""

from PySide6.QtCore import Qt
from PySide6.QtGui import (
    QColor,
    QFont,
    QPainter,
    QPen,
)
from PySide6.QtWidgets import QWidget
from src.services.slide_service import SlideService
from src.models.slide import Slide

from src.models.elements.text_element import TextElement
from src.models.elements.image_element import ImageElement
from PySide6.QtGui import QPixmap
from pathlib import Path
from src.services.element_service import ElementService

class SlidePreviewWidget(QWidget):

    DESIGN_WIDTH = 960
    DESIGN_HEIGHT = 540

    # -------------------------------------------------

    def __init__(self,app):

        super().__init__()

        self.app = app
        
        self.slide: Slide | None = None

        self.app.selection.selection_changed.connect(
    self.update
)

        self.page_rect = None

        self.scale_x = 1.0
        self.scale_y = 1.0

        self.setMinimumSize(420, 240)
        self.dragging = False

        self.drag_offset_x = 0
        self.drag_offset_y = 0

        self.element_service = app.services.get(
            ElementService
        )

        self.slide_service = app.services.get(
    SlideService
)
        
    # -------------------------------------------------

    def set_slide(self, slide: Slide | None):

        self.slide = slide

        self.app.selection.set_slide(slide)

        self.update()

    # -------------------------------------------------

    def paintEvent(self, event):

        painter = QPainter(self)

        painter.setRenderHint(QPainter.Antialiasing)
        painter.setRenderHint(QPainter.TextAntialiasing)

        painter.setRenderHint(QPainter.SmoothPixmapTransform)

        # Background

        painter.fillRect(
            self.rect(),
            QColor(180, 180, 180),
        )

        margin = 20

        available = self.rect().adjusted(
            margin,
            margin,
            -margin,
            -margin,
        )

        ratio = self.DESIGN_WIDTH / self.DESIGN_HEIGHT

        w = available.width()
        h = int(w / ratio)

        if h > available.height():
        
            h = available.height()

            w = int(h * ratio)

        x = available.left() + (available.width() - w) // 2

        y = available.top() + (available.height() - h) // 2

        page = available.adjusted(0, 0, 0, 0)

        page.setLeft(x)
        page.setTop(y)
        page.setWidth(w)
        page.setHeight(h)

        self.page_rect = page

        self.scale_x = page.width() / self.DESIGN_WIDTH

        self.scale_y = page.height() / self.DESIGN_HEIGHT

        # Paper
        shadow = page.translated(5, 5)

        painter.fillRect(
            shadow,
            QColor(150, 150, 150, 80),
        )

        painter.fillRect(
            page,
            QColor("white"),
        )

        painter.setPen(QPen(Qt.black, 1))

        painter.drawRect(page)

        if self.slide is None:

            return

        # Draw Elements

        for element in self.slide.elements:

            x = page.left() + element.x * self.scale_x
            y = page.top() + element.y * self.scale_y

            w = element.width * self.scale_x
            h = element.height * self.scale_y

            if isinstance(element, TextElement):

                self._draw_text(
                    painter,
                    element,
                    x,
                    y,
                    w,
                    h,
                )

            elif isinstance(element, ImageElement):

                self._draw_image(
                    painter,
                    element,
                    x,
                    y,
                    w,
                    h,
                )

            # Selection Rectangle

            if self.app.selection.is_selected(element):

                painter.setPen(
                    QPen(
                        QColor(0, 120, 255),
                        2,
                    )
                )

                painter.drawRect(
                    int(x),
                    int(y),
                    int(w),
                    int(h),
                )

    # -------------------------------------------------

    def _draw_text(
        self,
        painter,
        element,
        x,
        y,
        w,
        h,
    ):

        font = QFont(
            element.font_family,
            max(
                6,
                int(element.font_size * 0.45),
            ),
        )

        font.setBold(element.bold)
        font.setItalic(element.italic)
        font.setUnderline(element.underline)

        painter.setFont(font)

        painter.setPen(QColor(element.color))


        flags = Qt.TextWordWrap

        if element.alignment == "right":
            flags |= Qt.AlignRight

        elif element.alignment == "center":
            flags |= Qt.AlignHCenter

        else:
            flags |= Qt.AlignLeft

        painter.drawText(
            int(x),
            int(y),
            int(w),
            int(h),
            flags,
            element.text,
        )
    # -------------------------------------------------

    def _draw_image(
    self,
    painter,
    element,
    x,
    y,
    w,
    h,
):

    #
    # اگر فایل تصویر وجود دارد، خود تصویر را نمایش بده
    #

        if element.path and Path(element.path).exists():

            pixmap = QPixmap(element.path)

            painter.drawPixmap(

                int(x),

                int(y),

                int(w),

                int(h),

                pixmap,

            )

            return

        #
        # Placeholder
        #

        painter.setPen(QPen(Qt.darkGray, 1))

        painter.drawRect(

            int(x),

            int(y),

            int(w),

            int(h),

        )

        painter.drawText(

            int(x),

            int(y),

            int(w),

            int(h),

            Qt.AlignCenter,

            "IMAGE",

        )

        if element.caption:

            painter.drawText(

                int(x),

                int(y + h - 25),

                int(w),

                20,

                Qt.AlignCenter,

                element.caption,

            )

    # -------------------------------------------------

    def mousePressEvent(self, event):

        if self.slide is None:

            return

        if self.page_rect is None:

            return

        px = (
            event.position().x()
            - self.page_rect.left()
        ) / self.scale_x

        py = (
            event.position().y()
            - self.page_rect.top()
        ) / self.scale_y

        if not self.page_rect.contains(event.position().toPoint()):

            self.app.selection.clear_element()

            self.update()

            return

        #
        # Topmost element wins
        #

        for element in reversed(self.slide.elements):

            if element.contains(px,py,):

                self.app.selection.set_element(element)
                
                self.dragging = True

                self.drag_offset_x = px - element.x

                self.drag_offset_y = py - element.y

                break

        self.update()
    
    def mouseMoveEvent(self, event):

        if not self.dragging:

            return

        element = self.app.selection.current_element

        if element is None:
            return

        if self.page_rect is None:

            return

        px = (

            event.position().x()

            - self.page_rect.left()

        ) / self.scale_x

        py = (

            event.position().y()

            - self.page_rect.top()

        ) / self.scale_y

        new_x = px - self.drag_offset_x
        new_y = py - self.drag_offset_y

        new_x = max(
            0,
            min(
                new_x,
                self.DESIGN_WIDTH - element.width,
            ),
        )

        new_y = max(
            0,
            min(
                new_y,
                self.DESIGN_HEIGHT - element.height,
            ),
        )

        self.element_service.move(
            element,
            new_x,
            new_y,
        )

        self.update()
        
    def mouseReleaseEvent(self, event):
        
        if self.dragging and self.slide:

            self.slide_service.save_slide(
                self.slide
            )

        self.dragging = False

        self.update()
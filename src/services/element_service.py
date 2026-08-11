"""
PresentationAI

Element Service
"""

from __future__ import annotations

from copy import deepcopy
import uuid

from src.core.service import BaseService

from src.models.slide import Slide
from src.models.elements.element import Element
from src.services.commands.move_element_command import (
    MoveElementCommand,
)
from src.services.commands.resize_element_command import (
    ResizeElementCommand,
)

from src.services.commands.rotate_element_command import (
    RotateElementCommand,
)

class ElementService(BaseService):
    """
    Handles geometry operations on slide elements.

    This service is intentionally lightweight.

    Responsibilities:
        - Add / Delete
        - Duplicate
        - Move
        - Resize
        - Rotate
        - Z-Order

    Persistence is handled by SlideService.
    """
    def __init__(
    self,
    history_service=None,
):

        self.history = history_service
    # -------------------------------------------------

    def initialize(self):

        print("ElementService.initialize()")

    # -------------------------------------------------

    def shutdown(self):

        print("ElementService.shutdown()")
        
    
    # -------------------------------------------------

    def _push_history(
        self,
        command,
    ):

        if self.history is None:

            return

        self.history.push(command)

    # -------------------------------------------------
    # Add / Remove
    # -------------------------------------------------

    def add(
        self,
        slide: Slide,
        element: Element,
    ):

        if slide is None:

            return

        if element in slide.elements:

            return

        slide.elements.append(element)

    # -------------------------------------------------

    def delete(
        self,
        slide: Slide,
        element: Element,
    ):

        if slide is None:

            return

        if element not in slide.elements:

            return

        slide.elements.remove(element)

    # -------------------------------------------------
    # Duplicate
    # -------------------------------------------------

    def duplicate(
        self,
        slide: Slide,
        element: Element,
        offset: float = 20,
    ) -> Element:

        if slide is None:

            return None

        if element not in slide.elements:

            return None

        new_element = deepcopy(element)

        #
        # New identity
        #

        new_element.id = str(uuid.uuid4())

        new_element.selected = False

        #
        # Offset
        #

        new_element.move_by(
            offset,
            offset,
        )

        slide.elements.append(new_element)

        return new_element

    # -------------------------------------------------
    # Move
    # -------------------------------------------------

    def move(
        self,
        element: Element,
        x: float,
        y: float,
        record_history: bool = True,
    ):
    
        #
        # Nothing changed
        #
    
        if element.x == x and element.y == y:
        
            return
    
        old_x = element.x
        old_y = element.y
    
        element.move_to(
            x,
            y,
        )
    
        #
        # Register Undo command
        #
    
        if record_history:
        
            self._push_history(
            
                MoveElementCommand(

                        element=element,

                        old_x=old_x,
                        old_y=old_y,

                        new_x=x,
                        new_y=y,

                        service=self,

                    )
    
                )
    
            

    # -------------------------------------------------

    def move_by(
        self,
        element: Element,
        dx: float,
        dy: float,
    ):

        if element.locked:

            return

        element.move_by(
            dx,
            dy,
        )
    
        # -------------------------------------------------
    # Resize
    # -------------------------------------------------

    def resize(
        self,
        element: Element,
        width: float,
        height: float,
        record_history: bool = True,
    ):

        #
        # Nothing changed
        #

        if (
            element.width == width
            and
            element.height == height
        ):

            return

        old_width = element.width
        old_height = element.height

        element.resize(
            width,
            height,
        )

        if record_history:

            self._push_history(

                ResizeElementCommand(

                    element=element,

                    old_width=old_width,
                    old_height=old_height,

                    new_width=element.width,
                    new_height=element.height,

                    service=self,

                )

            )

    # -------------------------------------------------

    def resize_by(
        self,
        element: Element,
        dw: float,
        dh: float,
    ):

        if element.locked:

            return

        element.resize(
            element.width + dw,
            element.height + dh,
        )

    # -------------------------------------------------
    # Rotation
    # -------------------------------------------------

    def rotate(
        self,
        element: Element,
        angle: float,
        record_history: bool = True,
    ):
    
        #
        # Nothing changed
        #
    
        if element.rotation == angle:
        
            return
    
        old_rotation = element.rotation
    
        element.rotation = angle
    
        if record_history:
        
            self._push_history(
            
                RotateElementCommand(
                
                    element=element,
    
                    old_rotation=old_rotation,
    
                    new_rotation=angle,
    
                    service=self,
    
                )
    
            )

    # -------------------------------------------------
    # Z-Order
    # -------------------------------------------------

    def bring_forward(
        self,
        slide: Slide,
        element: Element,
    ):

        if slide is None:

            return

        if element not in slide.elements:

            return

        index = slide.elements.index(element)

        if index >= len(slide.elements) - 1:

            return

        slide.elements[index], slide.elements[index + 1] = (

            slide.elements[index + 1],

            slide.elements[index],

        )

    # -------------------------------------------------

    def send_backward(
        self,
        slide: Slide,
        element: Element,
    ):

        if slide is None:

            return

        if element not in slide.elements:

            return

        index = slide.elements.index(element)

        if index <= 0:

            return

        slide.elements[index], slide.elements[index - 1] = (

            slide.elements[index - 1],

            slide.elements[index],

        )

    # -------------------------------------------------

    def bring_to_front(
        self,
        slide: Slide,
        element: Element,
    ):

        if slide is None:

            return

        if element not in slide.elements:

            return

        slide.elements.remove(element)

        slide.elements.append(element)

    # -------------------------------------------------

    def send_to_back(
        self,
        slide: Slide,
        element: Element,
    ):

        if slide is None:

            return

        if element not in slide.elements:

            return

        slide.elements.remove(element)

        slide.elements.insert(
            0,
            element,
        )
        
        # -------------------------------------------------
    # Queries
    # -------------------------------------------------

    def contains(
        self,
        slide: Slide,
        element: Element,
    ) -> bool:

        if slide is None:

            return False

        return element in slide.elements

    # -------------------------------------------------

    def count(
        self,
        slide: Slide,
    ) -> int:

        if slide is None:

            return 0

        return len(slide.elements)

    # -------------------------------------------------

    def index_of(
        self,
        slide: Slide,
        element: Element,
    ) -> int:

        if slide is None:

            return -1

        try:

            return slide.elements.index(element)

        except ValueError:

            return -1

    # -------------------------------------------------

    def clear(
        self,
        slide: Slide,
    ):

        if slide is None:

            return

        slide.elements.clear()

    # -------------------------------------------------

    def get_all(
        self,
        slide: Slide,
    ) -> list[Element]:

        if slide is None:

            return []

        return slide.elements

    # -------------------------------------------------

    def get(
        self,
        slide: Slide,
        index: int,
    ) -> Element | None:

        if slide is None:

            return None

        if 0 <= index < len(slide.elements):

            return slide.elements[index]

        return None
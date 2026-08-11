"""
PresentationAI

Resize Element Command
"""

from __future__ import annotations

from src.models.elements.element import Element
from src.services.commands.command import Command


class ResizeElementCommand(Command):
    """
    Undo/Redo command for resizing an element.
    """

    # -------------------------------------------------

    def __init__(
        self,
        element: Element,
        old_width: float,
        old_height: float,
        new_width: float,
        new_height: float,
        service,
    ):

        self.element = element

        self.service = service

        self.old_width = old_width
        self.old_height = old_height

        self.new_width = new_width
        self.new_height = new_height

    # -------------------------------------------------

    def undo(self):

        self.service.resize(

            self.element,

            self.old_width,

            self.old_height,

            record_history=False,

        )

    # -------------------------------------------------

    def redo(self):

        self.service.resize(

            self.element,

            self.new_width,

            self.new_height,

            record_history=False,

        )
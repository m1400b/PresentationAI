"""
PresentationAI

Move Element Command
"""

from __future__ import annotations

from src.models.elements.element import Element
from src.services.commands.command import Command


class MoveElementCommand(Command):
    """
    Undo/Redo command for moving an element.
    """

    # -------------------------------------------------

    def __init__(
        self,
        element,
        old_x,
        old_y,
        new_x,
        new_y,
        service,
    ):

        self.element = element

        self.service = service

        self.old_x = old_x
        self.old_y = old_y

        self.new_x = new_x
        self.new_y = new_y

    # -------------------------------------------------

    def undo(self):

        self.service.move(

            self.element,

            self.old_x,

            self.old_y,

            record_history=False,

        )

    # -------------------------------------------------

    def redo(self):

        self.service.move(

            self.element,

            self.new_x,

            self.new_y,

            record_history=False,

        )
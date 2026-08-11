"""
PresentationAI

Rotate Element Command
"""

from __future__ import annotations

from src.models.elements.element import Element
from src.services.commands.command import Command


class RotateElementCommand(Command):
    """
    Undo/Redo command for rotating an element.
    """

    # -------------------------------------------------

    def __init__(
        self,
        element: Element,
        old_rotation: float,
        new_rotation: float,
        service,
    ):

        self.element = element

        self.service = service

        self.old_rotation = old_rotation

        self.new_rotation = new_rotation

    # -------------------------------------------------

    def undo(self):

        self.service.rotate(

            self.element,

            self.old_rotation,

            record_history=False,

        )

    # -------------------------------------------------

    def redo(self):

        self.service.rotate(

            self.element,

            self.new_rotation,

            record_history=False,

        )
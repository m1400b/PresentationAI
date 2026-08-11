"""
PresentationAI

Base Command
"""

from __future__ import annotations


class Command:
    """
    Base class for every undo/redo command.
    """

    # -------------------------------------------------

    def undo(self):

        raise NotImplementedError

    # -------------------------------------------------

    def redo(self):

        raise NotImplementedError
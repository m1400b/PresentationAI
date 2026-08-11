"""
PresentationAI

History Service
"""

from __future__ import annotations

from copy import deepcopy

from src.core.service import BaseService


class HistoryService(BaseService):
    """
    Generic Undo / Redo history.

    Stores immutable snapshots of any object.

    Usually PresentationDocument.
    """

    # -------------------------------------------------

    def __init__(
        self,
        max_history: int = 50,
    ):

        self.max_history = max_history

        self._history = []

        self._future = []

    # -------------------------------------------------

    def initialize(self):

        print("HistoryService.initialize()")

    # -------------------------------------------------

    def shutdown(self):

        print("HistoryService.shutdown()")

        self.clear()

    # -------------------------------------------------
    # State
    # -------------------------------------------------

    def clear(self):

        self._history.clear()

        self._future.clear()

    # -------------------------------------------------

    def push(
        self,
        state,
    ):
        """
        Save current state.

        Calling push() clears redo history.
        """

        if state is None:

            return

        snapshot = deepcopy(state)

        self._history.append(snapshot)

        self._future.clear()

        #
        # Limit history size
        #

        if len(self._history) > self.max_history:

            self._history.pop(0)

    # -------------------------------------------------

    def current(self):

        if not self._history:

            return None

        return deepcopy(
            self._history[-1]
        )
    
        # -------------------------------------------------
    # Undo / Redo
    # -------------------------------------------------

    def can_undo(self) -> bool:

        #
        # At least two states are required.
        #
        # Current + Previous
        #

        return len(self._history) > 1

    # -------------------------------------------------

    def can_redo(self) -> bool:

        return len(self._future) > 0

    # -------------------------------------------------

    def undo(self):
        """
        Returns previous snapshot.

        Current snapshot is moved
        to the redo stack.
        """

        if not self.can_undo():

            return None

        #
        # Current -> Future
        #

        current = self._history.pop()

        self._future.append(current)

        #
        # Previous becomes current
        #

        return deepcopy(
            self._history[-1]
        )

    # -------------------------------------------------

    def redo(self):
        """
        Restores the last undone snapshot.
        """

        if not self.can_redo():

            return None

        state = self._future.pop()

        self._history.append(state)

        return deepcopy(state)
        # -------------------------------------------------
    # Information
    # -------------------------------------------------

    @property
    def history_size(self) -> int:

        return len(self._history)

    # -------------------------------------------------

    @property
    def future_size(self) -> int:

        return len(self._future)

    # -------------------------------------------------

    @property
    def is_empty(self) -> bool:

        return len(self._history) == 0

    # -------------------------------------------------

    def __len__(self):

        return len(self._history)

    # -------------------------------------------------

    def __repr__(self):

        return (
            f"<HistoryService "
            f"history={self.history_size} "
            f"future={self.future_size}>"
        )
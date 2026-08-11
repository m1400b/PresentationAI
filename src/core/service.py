"""
PresentationAI

Base Service
"""

from abc import ABC


class BaseService(ABC):
    """
    Base class for all application services.
    """

    def __init__(self):

        self._initialized = False

    # -------------------------------------------------

    def initialize(self):

        self._initialized = True

    # -------------------------------------------------

    def shutdown(self):

        self._initialized = False

    # -------------------------------------------------

    @property
    def initialized(self):

        return self._initialized
"""
PresentationAI

Base Layout
"""

from abc import ABC, abstractmethod


class BaseLayout(ABC):

    @abstractmethod
    def build(self, draft):
        pass
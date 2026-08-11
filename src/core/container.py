"""
PresentationAI

Service Container
"""

from typing import Any


class ServiceContainer:
    """
    Dependency Injection Container
    """

    def __init__(self):

        self._services: dict[type, Any] = {}

    # ----------------------------------------------------

    def register(self, service_type, instance):

        self._services[service_type] = instance

    # ----------------------------------------------------

    def get(self, service_type):

        if service_type not in self._services:

            raise KeyError(
                f"{service_type.__name__} is not registered."
            )

        return self._services[service_type]

    # ----------------------------------------------------

    def exists(self, service_type):

        return service_type in self._services

    # ----------------------------------------------------

    def clear(self):

        self._services.clear()
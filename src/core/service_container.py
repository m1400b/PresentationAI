"""
PresentationAI

Service Container
"""

from __future__ import annotations


class ServiceContainer:
    """
    Dependency Injection Container.

    Responsible for:
        - Register services
        - Resolve services
        - Manage lifecycle
    """


    def __init__(self):

        self._services = {}


    # -------------------------------------------------

    def register(
        self,
        service_type,
        instance,
    ):
        """
        Registers service instance.
        """

        self._services[service_type] = instance


    # -------------------------------------------------

    def get(
        self,
        service_type,
    ):
        """
        Resolves service instance.
        """

        if service_type not in self._services:

            raise KeyError(
                f"Service not registered: {service_type}"
            )

        return self._services[service_type]


    # -------------------------------------------------

    def has(
        self,
        service_type,
    ) -> bool:

        return service_type in self._services
    
    def exists(
        self,
        service_type,
    ) -> bool:

        return self.has(
            service_type
        )


    # -------------------------------------------------

    def initialize_all(self):

        for service in self._services.values():

            if hasattr(
                service,
                "initialize",
            ):

                service.initialize()


    # -------------------------------------------------

    def shutdown_all(self):

        for service in reversed(
            list(self._services.values())
        ):

            if hasattr(
                service,
                "shutdown",
            ):

                service.shutdown()


    # -------------------------------------------------

    def clear(self):

        self._services.clear()


    # -------------------------------------------------

    def __len__(self):

        return len(
            self._services
        )


    # -------------------------------------------------

    def __repr__(self):

        return (
            f"<ServiceContainer "
            f"services={len(self)}>"
        )
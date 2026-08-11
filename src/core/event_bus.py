"""
PresentationAI

Event Bus
"""


class EventBus:

    def __init__(self):

        self._events = {}

    # -----------------------------------------

    def subscribe(self, event_name, callback):

        self._events.setdefault(event_name, [])

        self._events[event_name].append(callback)

    # -----------------------------------------

    def emit(self, event_name, *args, **kwargs):

        callbacks = self._events.get(event_name, [])

        for callback in callbacks:

            callback(*args, **kwargs)

    # -----------------------------------------

    def unsubscribe(self, event_name, callback):

        if event_name not in self._events:

            return

        if callback in self._events[event_name]:

            self._events[event_name].remove(callback)
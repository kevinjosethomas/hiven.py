class EventError(Exception):
    """Base class for event-related exceptions"""

    pass


class EventHandlerError(EventError):
    """Class for event handler related exceptions"""

    pass

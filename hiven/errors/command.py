from hiven.errors.base import HivenError


class CommandError(HivenError):
    """Base class for command-related exceptions"""

    pass


class CommandAlreadyExists(CommandError):
    """Triggered when there is a conflicting name or alias between multiple commands"""

    pass


class MissingRequiredArgument(CommandError):
    """Triggered when a required argument is missing on command execution"""

    pass


class ArgumentParsingError(CommandError):
    """Triggered when a command's argument cannot be parsed due to user input"""

    pass

from typing import Coroutine, List


class Command:
    def __init__(
        self, name: str, function: Coroutine, arguments: List[tuple], description: str, usage: str, aliases: List[str]
    ):
        self.name = name
        self.description = description
        self.usage = usage
        self.aliases = aliases

        self.function = function
        self.arguments = arguments

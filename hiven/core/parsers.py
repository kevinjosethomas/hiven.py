from hiven.errors import ArgumentParsingError


class Parser:
    """Base class for all parsers"""

    @staticmethod
    def parse(ctx, argument: str):
        pass

    pass


class String(Parser):
    """Class to parse string arguments"""

    def parse(ctx, argument):
        return str(argument.strip())


class Integer(Parser):
    """Class to parse integer arguments"""

    def parse(ctx, argument):
        try:
            return int(argument.strip())
        except ValueError:
            raise ArgumentParsingError()


class Boolean(Parser):
    """Class to parse boolean arguments"""

    def parse(ctx, argument):
        arg = argument.lower().strip()

        if arg in ["true", "yes", "on"]:
            return True
        elif arg in ["false", "no", "off"]:
            return False
        else:
            raise ArgumentParsingError()


TYPE_CONVERTERS = {str: String, int: Integer, bool: Boolean}

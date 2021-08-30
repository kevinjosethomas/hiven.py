import traceback

def format_exception(e: Exception) -> str:
     return "".join(traceback.format_exception(type(e), e, e.__traceback__, 4))

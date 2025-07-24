import sys
from functools import partial

from click import echo, style


def color(message: str, end: bool = True, fg: str = "white") -> None:
    echo(message=style(text=message, fg=fg), color=True)
    if end:
        sys.exit(0)


red = partial(color, fg="red", end=True)
green = partial(color, fg="green", end=False)

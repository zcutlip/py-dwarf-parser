from pydwarf.__about__ import (
    __version__,
    __title__,
    __summary__
)


def version():
    return "%s %s" % (__title__, __version__)


def about():
    return ("%s\n%s" % (version(), __summary__))


__all__ = [
    "__version__",
    "__title__",
    "__summary__"
]

import os
import platform

impl = platform.python_implementation()


def _should_use_cffi() -> bool:
    ev = os.getenv("LZF_USE_CFFI")
    if ev is not None:
        return True
    if impl == "CPython":
        return False
    else:
        return True


if not _should_use_cffi():
    from pylzf.backends.cython import *
else:
    from pylzf.backends.cffi import *

__version__ = "0.1.1"

from collections.abc import Callable
import functools
import time
from typing import Optional


def sleep_with_arg(_fucn: Optional[Callable] = None, *, sec=1) -> Callable:
    """
    Decorator that takes argument for seconds: It must be named one
        use example: "@sleep_with_arg(sec=12)"

    """
    def sleep(func: Callable) -> Callable:

        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            time.sleep(sec)
            func(*args, **kwargs)
        return wrapper
    if _fucn is None:
        return sleep
    return sleep(_fucn)


@sleep_with_arg(sec=3)
def pr():
    print("Here we go!")

pr()

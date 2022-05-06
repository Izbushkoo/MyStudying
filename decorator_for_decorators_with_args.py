import functools
from typing import Callable


def decorator_with_args_for_any_decorator(decorator: Callable) -> Callable:
    """
    Decorator for decorators. Makes it possible for any of them to take
    any arguments and keyword-arguments.

    """

    def decorator_maker(*args, **kwargs):
        @functools.wraps(decorator)
        def wrapper(func):
            return decorator(func, *args, **kwargs)
        return wrapper
    return decorator_maker


@decorator_with_args_for_any_decorator
def decorated_decorator(func: Callable, *args, **kwargs) -> Callable:
    """Decorator for function that prints  passed arguments and keyword-arguments."""

    print("Passed args and kwargs:", args, kwargs)

    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        new = func(*args, **kwargs)
        return new
    return wrapper


@decorated_decorator(100, 'rubles', 200, "friends")
def decorated_function(text: str, num: int) -> None:
    print("Hello", text, num)


decorated_function('User', 101)

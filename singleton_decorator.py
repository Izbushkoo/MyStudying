import functools
from typing import Callable


def singleton(cls: Callable) -> Callable:
    """Decorator that represents singleton-pattern."""
    check_list = []

    @functools.wraps(cls)
    def wrapper(*args, **kwargs):  # Just follow the templates of decorator.
        # In here args and kwargs useless.
        if len(check_list) == 0:
            check_list.append(cls)
            return check_list[0]
        else:
            return check_list[0]
    return wrapper


@singleton
class Example:
    pass


my_obj = Example()
my_another_obj = Example()

print(id(my_obj))
print(id(my_another_obj))

print(my_obj is my_another_obj)


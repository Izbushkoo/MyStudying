import functools
import time
from datetime import datetime
from collections.abc import Callable


def write_log(func: Callable) -> Callable:
    """
    Decorator that writes data and time of a method call, method name
    into "methods_log.log" file

    """
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        try:
            open('methods_log.log', 'x')
        except FileExistsError:
            pass
        finally:
            with open('methods_log.log', 'a') as log:
                message = '[{time}] ==> {meth}\n'.format(
                    time=datetime.utcnow().strftime('%d/%m/%Y  %H:%M:%S'),
                    meth=func.__name__
                )
                log.write(message)
    return wrapper


def logging(decorator: Callable) -> Callable:
    """
    Decorator for class that wraps every method inside.

    """
    @functools.wraps(decorator)
    def wrapper(cls):
        for i_method in dir(cls):
            if i_method.startswith('__') is False:
                cur_method = getattr(cls, i_method)
                dec_method = decorator(cur_method)
                setattr(cls, i_method, dec_method)
        return cls
    return wrapper


@logging(write_log)
class Mine:

    def __init__(self, number: int) -> None:
        self.number = number

    def squares(self) -> int:
        return sum(x ** 2 for x in range(1, self.number))

    def cubes(self) -> int:
        return sum(x ** 3 for x in range(1, self.number))


cl = Mine(5)
time.sleep(2)
cl.cubes()
time.sleep(1)
cl.squares()

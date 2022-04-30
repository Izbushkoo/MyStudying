import functools
from typing import Callable, Any, Optional


def debug(func: Callable) -> Callable:
    """
    Decorator that prints function's title with all passed arguments, then prints returned
    value of the function, and then result of its evaluation.

    """

    @functools.wraps(func)
    def wrapper(*args, **kwargs) -> Any:
        """
        Wrapper.
        Local variable arguments: A list of all arguments of passed, that is used for creating
        a representation string.

        """
        def representation() -> str:
            """
            Make a string of representation according to passed arguments using 'locals()' method.

            """
            string = "{func_name}".format(func_name=func.__name__)
            if arguments:
                string += '(' + ', '.join(arguments) + ')'
            return string

        arguments = [repr(elem) for elem in locals()['args']] + [
            '{key}={value}'.format(key=key, value=value)
            for key, value in locals()['kwargs'].items()
        ]

        print("\nCalls function", representation())
        print("Function returned value:", repr(func(*args, **kwargs)))
        print(func(*args, **kwargs))

    return wrapper


@debug
def greeting(name: str, age: Optional[int] = None) -> str:
    if age:
        return "Wow, {name}! You are {age}, fast growing up.".format(name=name, age=age)
    else:
        return "Hello, {name}!".format(name=name)


greeting("Smb")
greeting("Gena", age=100)
greeting(name="Kate", age=16)

import functools
from typing import Callable


def counter(func: Callable, count_lst=dict()) -> Callable:  # Dangerous trait was chosen to use=)
    # The first thought that my mind caught without using global.

    """
    Counter of decorated function calls. Is used default 'dict' argument that contains name of
    called function as a key, and value as a counter. So it counts separately different functions.

    """
    @functools.wraps(func)
    def wrapper(*args, **kwargs) -> None:

        if func.__name__ not in count_lst.keys():
            count_lst[func.__name__] = 1
        else:
            count_lst[func.__name__] += 1

        func(*args, **kwargs)
        print("Number of calls of the function:", count_lst.get(func.__name__))

    return wrapper


@counter
def main() -> None:
    print("Something is going on...")


@counter
def one_more() -> None:
    print("one more")


for _ in range(5):
    main()

for _ in range(3):
    one_more()
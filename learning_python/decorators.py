from functools import wraps
from typing import Callable


def repeat(fun: Callable = None, *, times=2) -> Callable:
    if fun is None:
        return lambda f: repeat(f, times=times)

    @wraps(fun)
    def g(*args, **kwargs):
        for i in range(times):
            fun(*args, **kwargs)

    return g


@repeat
def f():
    print("Hello f!")

f()


@repeat(times=3)
def g():
    print("Hello g!")


g()
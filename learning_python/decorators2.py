from functools import wraps
from typing import Callable


def augment(fun: Callable = None, *, increment=1) -> Callable:
    if fun is None:
        return lambda f: augment(f, increment=increment)

    @wraps(fun)
    def g(*args, **kwargs):
        return fun(*args, **kwargs) + increment

    return g


@augment
def f():
    return 5


assert f() == 6


@augment
def g(x, y):
    """Add two numbers."""
    return x + y


assert g(1, 2) == 4


@augment(increment=3)
def f():
    return 5


assert f() == 8


@augment(increment=2)
def g(x, y):
    """Add two numbers."""
    return x + y


assert g(1, 2) == 5

###########

def f():
    return 5

def g(x, y):
    """Add two numbers."""
    return x + y

assert augment(f)() == 6
assert augment(g)(1, 2) == 4
assert augment(increment=3)(f)() == 8
assert augment(increment=2)(g)(1, 2) == 5

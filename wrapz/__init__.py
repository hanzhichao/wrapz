from functools import wraps


def wrapz(func, *args, **kwargs):
    print(func.__name__)
    @wraps(func)
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return result
    return wrapper


@wrapz
def add(a, b):
    return a+b



print(add(1,3))

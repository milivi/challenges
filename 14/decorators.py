from functools import wraps


def true_false(func):
    """Changes return value to True or False based on the 'truthy' value of the object."""
    @wraps(func)  # preserves function meta data
    def wrapper(*args, **kwargs):
        return bool(func(*args, **kwargs))
    return wrapper


def upper_in_title_out(func):
    """Changes the input string(s) to uppercase and the output string to title case."""
    @wraps(func)
    def wrapper(*args, **kwargs):
        upper_args = [arg.upper() for arg in args]
        for keyword, value in kwargs.items():
            kwargs[keyword] = value.upper()
        return func(*upper_args, **kwargs).title()
    return wrapper

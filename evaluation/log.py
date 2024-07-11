from functools import wraps


def log_vars(logfile: str = 'out.log'):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            print('start', func.__name__, args, kwargs)
            result = func(*args, **kwargs)
            print('end', func.__name__, args, kwargs)
            return result
        return wrapper
    return decorator


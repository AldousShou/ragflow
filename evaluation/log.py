from functools import wraps
import pymysql
# connect to mysql

conn = pymysql.connect(
    host='192.168.88.99',
    port=3306,
    user='root',
    password='aa123456',
    database='dbgpt',
)
cur = conn.cursor()


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

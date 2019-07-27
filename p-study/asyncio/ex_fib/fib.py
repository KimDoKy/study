from functools import wraps
from time import time

def log_execution_time(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time()
        return_value = func(*agrs, **kwargs)
        message = "Executing {} took {:.03} seconds.".format(func.__name__, time()-start)
        print(message)
        return return_value
    return wrapper

def fib(n):
    return fib(n-1) + fib(n-2) if n > 1 else n

timed_fib = log_execution_time(fib)

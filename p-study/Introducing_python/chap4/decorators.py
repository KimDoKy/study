# Decorator

def document_it(func):
    def new_func_docu(*args, **kwargs):
        print('Running func: ', func.__name__)
        print('args: ', *args)
        print('kwargs: ', **kwargs)
        result = func(*args, **kwargs)
        print('Result: ', result)
        return result
    return new_func_docu

def square_it(func):
    def new_func_sq(*args, **kwargs):
        result = func(*args, **kwargs)
        return result * result
    return new_func_sq

print('---1--')

@document_it
@square_it
def add_ints(a, b):
    return a + b

add_ints(3, 5)

print('---2---')
@square_it
@document_it
def add_ints(a, b):
    return a + b

add_ints(3, 5)

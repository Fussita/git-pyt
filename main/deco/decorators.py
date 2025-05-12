
"""
    from functools import wraps

    ESTO SIRVE PARA NO PERDER LOS METADATOS DE LAS FUNCIONES
    def my_decorator(function):
    @wraps(function)
    def wrapper(*args, **kwards):
        return function(*args, **kwards)
    return wrapperw
"""

# LOS DECORADORES SE APLICAN DE ABAJO HACIA ARRIBA
def logger(function):
    def wrapper():
        func = function()
        print('LOGGING')
        return func
    return wrapper()

@logger
def say_hi():
    return 'hello there'

# but without @logger
decorate = logger(say_hi)
decorate()


# ARGUMENTS
def my_decorator(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return result
    return wrapper

@my_decorator
def greet(name):
    print(f"Hello, {name}!")

# DECORATOR CON ARGS
def repeat_decorator(times):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for _ in range(times):
                result = func(*args, **kwargs)
            return result
        return wrapper
    return decorator

@repeat_decorator(3)
def greet(name):
    print(f"Hello, {name}!")


"""
from functools import lru_cache
@lru_cache(maxsize=32)
def fibonacci(n):
print(fibonacci.cache_info())
"""

"""
        import time
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"{func.__name__} took {end_time - start_time} seconds to execute")
"""

""" VALIDATE DECORATORS
        #for arg in args:
        #    if not isinstance(arg, int) or arg < 0:
        #        raise ValueError("All arguments must be non-negative integers")
        
"""
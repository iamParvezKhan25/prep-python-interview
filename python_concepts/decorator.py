import time


def execution_time(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        func(*args, **kwargs)
        end_time = time.time()

        actual_time = end_time - start_time
        print(f'function :{func.__name__} takes a {actual_time:.2f} second.')

    return wrapper


def namaste(func):
    def wrapper(*args, **kwargs):
        print("Namaste World!")
        func(*args, **kwargs)
    return wrapper


@execution_time
@namaste
def hello():
    time.sleep(1)
    print("Hello World!")


hello()

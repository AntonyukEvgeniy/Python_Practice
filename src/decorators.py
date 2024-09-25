from functools import wraps


def log(file=""):
    def logger(func):
        @wraps(func)
        def wrapped(*args, **kwargs):
            try:
                func(*args, **kwargs)
                if file != "":
                    f = open(file, "a")
                    f.write(f"\n{func.__name__} ok")
                else:
                    print(f"{func.__name__} ok")
            except Exception as e:
                if file != "":
                    f = open(file, "a")
                    f.write(f"\n{func.__name__} error: {repr(e)}. Inputs: {args}, {kwargs}")
                else:
                    print(f"{func.__name__} error: {repr(e)}. Inputs: {args}, {kwargs}")
            return func(*args, **kwargs)

        return wrapped

    return logger

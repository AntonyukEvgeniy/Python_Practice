from functools import wraps
from typing import Any


def log(file:str="")->Any:
    """
    Декоратор, который логирует выполнение функции в файл либо в консоль, в зависимости от параметра file
    Ожидаемый вывод в лог-файл mylog.txt
    при успешном выполнении:
    my_function ok
    Ожидаемый вывод при ошибке:
    my_function error: тип ошибки. Inputs: (1, 2), {}
    """

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

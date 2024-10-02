import pytest

from src.decorators import log


@log("")
def log_function():
    return None


def test_log_decorator(capsys):
    log_function()
    captured = capsys.readouterr()
    assert captured.out == "log_function ok\n"


@log("")
def log_function_error():
    raise ValueError("Проверка записи ошибки в консоль")


def test_log_decorator_error(capsys):
    with pytest.raises(Exception, match="Проверка записи ошибки в консоль"):
        log_function_error()
    captured = capsys.readouterr()
    assert captured.out == "log_function_error error: ValueError('Проверка записи ошибки в консоль'). Inputs: (), {}\n"


@log("mylog.txt")
def test_log_function_with_file():
    return None


@log("mylog.txt")
def log_function_with_file_error():
    raise ValueError("Проверка записи ошибки в файл")


def test_log_decorator_with_file():
    test_log_function_with_file()
    with open("mylog.txt", "r") as f:
        last_line = f.readlines()[-1]
        assert last_line == "test_log_function_with_file ok"


def test_log_decorator_with_file_error():
    with pytest.raises(Exception, match="Проверка записи ошибки в файл"):
        log_function_with_file_error()
    with open("mylog.txt", "r") as f:
        last_line = f.readlines()[-1]
        assert (
            last_line
            == "log_function_with_file_error error: ValueError('Проверка записи ошибки в файл'). Inputs: (), {}"
        )

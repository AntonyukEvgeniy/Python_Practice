# Виджет банковских операций клиента
Банковский виджет, который отображает историю платежей пользователя в режиме реального времени. 

## Содержание
- [Технологии](#технологии)
- [Чтение файлов](#чтение-файлов-csv-и-excel)
- [Генератор](#генератор)
- [Декоратор log](#декоратор)
- [Тестирование](#тестирование)
- [Команда проекта](#команда-проекта)

## Технологии
- [Python](https://www.python.org/)
## Чтение файлов csv и excel
Добавлены 2 новые функции для чтения данных из файлов. 
1. В примере, получаем список транзакций(в виде словарей) из файла "data/transactions.csv"
```sh
print(get_transactions_from_csv_file("data/transactions.csv"))
```
2. В данном примере читаем excel-файл с транзакциями. Данные так же представлены в виде списка словарей. 
Значения null преобразованы к пустым строкам.  
```sh
print(get_transactions_from_xlsx_file("data/transactions_excel.xlsx"))
```
## Генератор
Генератор - новый модуль в проекте, который добавляет следующий функционал:
 1. Генерация номеров карт в заданном диапазоне. Пример:
    ```sh
    for card_number in card_number_generator(1, 5):
      print(card_number)
    ```
    Результат:\
    0000 0000 0000 0001\
    0000 0000 0000 0002\
    0000 0000 0000 0003\
    0000 0000 0000 0004\
    0000 0000 0000 0005
 2. Фильтрация транзакций по коду валюты. Пример:
    ```sh
    usd_transactions = filter_by_currency(transactions, "USD")
    for _ in range(2):
      print(next(usd_transactions))
    ```
 3. Генератор описания транзакций. Пример: 
    ```sh
    descriptions = transaction_descriptions(transactions)
    for _ in range(4):
      print(next(descriptions))
    ```
 
## Декоратор log
Декоратор log(file="filename") логирует выполнение функции в файл, который расположен в /filename. 
Если файл не указан, то лог записывается в консоль.\
Пример работы декоратора, с записью в консоль:
```sh
def test_log_decorator(capsys):
    test_log_function()
    captured = capsys.readouterr()
    assert captured.out == "test_log_function_error ok\n"
```


## Тестирование
В проекте используется pytest. 

Основные функции покрыты тестами с параметрами. Для генерации отчета в html запустите команду:
```sh
pytest --cov=src --cov-report=html
```
Запуск тестов:
```sh
pytest tests
pytest -k test_name
```

### Зачем вы разработали этот проект?
Это тренировочный проект для обучения языку Python

## Команда проекта
Оставьте пользователям контакты и инструкции, как связаться с командой разработки.

- [Антонюк Евгений](evgeniiantonyuk@gmail.com) — BE Engineer


import json


def load_data():
    """
    Выводит в список информацию о транзакциях файла "operations.json"
    """
    with open("operations.json") as file:
        operations = json.load(file)
        return operations


def get_correct_date(operations):
    """
    Выводит дату в правильном формате ДД.ММ.ГГГГ
    """
    date = operations["date"].split("T")[0]
    return f"{date[8:10]}.{date[5:7]}.{date[0:4]}"



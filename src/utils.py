import json


def load_data():
    """
    Выводит в список информацию о транзакциях файла "operations.json"
    :return:
    """
    with open("operations.json") as file:
        operations = json.load(file)
        return operations


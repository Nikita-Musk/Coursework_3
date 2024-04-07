import json


def load_data():
    """
    Выводит в список информацию о транзакциях файла "operations.json"
    """
    with open("operations.json") as file:
        operations = json.load(file)
        return operations


def get_correct_date(date):
    """
    Выводит дату в правильном формате ДД.ММ.ГГГГ
    """
    return f"{date[8:10]}.{date[5:7]}.{date[0:4]}"


def mask_card_number(card_number):
    """
    Выводит маску номера карты отправителя в формате "0000 00** **** 0000"
    """
    return f"{card_number[:4]} {card_number[4:6]}** **** {card_number[-4:]}"


def mask_account_number(account_number):
    """
    Выводит номер счета получателя в формате "**0000"
    """
    return f"**{account_number[-4:]}"


def format_operations(operations):
    """
    Форматирует информацию о банковской операции в удобночитаемый вид
    """

    # Проверка на наличие ключей "date", "description" и "operationAmount"
    # if "date" not in operations or "description" not in operations or "operationAmount" not in operations:
    #     raise ValueError("Некорректный формат данных операции")

    # Получение корректной даты операции
    date = get_correct_date(operations["date"].split("T")[0])

    # Получение описания операции
    description = operations["description"]

    # Получение информации об отправителе
    from_info = operations.get("from", "").split()
    sender = ' '.join(from_info[0:-1])
    card_number = mask_card_number(from_info[-1])

    # Получение информации о получателе
    to_info = operations.get("to", "").split()
    receiver = ' '.join(to_info[0:-1])
    account_number = mask_account_number(to_info[-1])

    # Получение суммы и валюты операции
    amount = operations["operationAmount"]["amount"]
    currency = operations["operationAmount"]["currency"]["name"]

    return f"{date} {description}\n{sender} {card_number} -> {receiver} {account_number}\n{amount} {currency}"




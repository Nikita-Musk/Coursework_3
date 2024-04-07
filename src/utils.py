import json


def load_data(file_path):
    """
    Выводит в список информацию о транзакциях файла "operations.json"
    """
    with open(file_path, 'r') as file:
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
    # Получение корректной даты операции
    date = get_correct_date(operations["date"].split("T")[0])

    # Получение описания операции
    description = operations["description"]

    # Получение информации об отправителе, обработка ошибки при отсутвии данных
    from_info = operations.get("from", "").split()
    sender = ' '.join(from_info[0:-1]) if len(from_info) > 1 else 'Номер карты отсутсвует'
    card_number = mask_card_number(from_info[-1]) if from_info else ''

    # Получение информации о получателе, обработка ошибки при отсутвии данных
    to_info = operations.get("to", "").split()
    receiver = ' '.join(to_info[0:-1]) if len(to_info) > 1 else 'Номер счета отсутсвует'
    account_number = mask_account_number(to_info[-1]) if to_info else ''

    # Получение суммы и валюты операции
    amount = operations["operationAmount"]["amount"]
    currency = operations["operationAmount"]["currency"]["name"]

    return f"{date} {description}\n{sender} {card_number} -> {receiver} {account_number}\n{amount} {currency}"


def prepare_operations(operations):
    """
    Форматирует информацию о 5 последних выполненных операциях.
    """
    executed_operations = []

    # Проверяем наличие ключа 'state' и выполнения операции
    for operation in operations:
        if "state" in operation and operation["state"] == "EXECUTED":
            executed_operations.append(operation)

    # Сортируем операции по дате
    sorted_operations = sorted(executed_operations, key=lambda x: x["date"], reverse=True)

    # Получаем 5 последних операций
    last_operations = sorted_operations[:5]

    # Форматируем операции по специальному формату функции format_operations()
    formatted_operations = [format_operations(operation) for operation in last_operations]
    return '\n\n'.join(formatted_operations)

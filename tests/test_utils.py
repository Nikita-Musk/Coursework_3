import os
import pytest
import json
from config import ROOT_DIR
from src.utils import (load_data,
                       get_correct_date,
                       mask_card_number,
                       mask_account_number,
                       prepare_operations,
                       format_operations)


@pytest.fixture()
def test_data():
    """
    Фикстура используется для предоставления тестовых данных, необходимых для выполнения тестов
    """
    DATA_PATH = os.path.join(ROOT_DIR, 'tests', 'test_operations.json')
    with open(DATA_PATH) as file:
        operations = json.load(file)
        return operations


def test_load_data(test_data):
    """
    Тест для функции load_data()
    """
    DATA_PATH = os.path.join(ROOT_DIR, 'tests', 'test_operations.json')
    assert load_data(DATA_PATH) == test_data


def test_get_correct_date(test_data):
    """
    Тест для функции get_correct_date()
    """
    date = test_data[0]["date"]
    assert get_correct_date(date) == "26.08.2019"


def test_mask_card_number(test_data):
    """
    Тест для функции mask_card_number()
    """
    card_number = test_data[0]["from"].split()[-1]
    assert mask_card_number(card_number) == "1596 83** **** 5199"


def test_mask_account_number(test_data):
    """
    Тест для функции mask_account_number()
    """
    account_number = test_data[0]["to"].split()[-1]
    assert mask_account_number(account_number) == "**9589"


def test_format_operation(test_data):
    """
    Тест для функции format_operation()
    """
    operation = test_data[0]
    assert format_operations(
        operation) == '26.08.2019 Перевод организации\nMaestro 1596 83** **** 5199 -> Счет **9589\n31957.58 руб.'


def test_prepare_operations(test_data):
    """
    Тест для функции prepare_operations()
    """
    # Получаем выполненые операции
    executed_operations = []
    for operation in test_data:
        if "state" in operation and operation["state"] == "EXECUTED":
            executed_operations.append(operation)

    # Сортируем по дате
    sorted_operations = sorted(executed_operations, key=lambda x: x["date"], reverse=True)

    # Получаем 5 последних
    last_operations = sorted_operations[:5]

    # Форматируем
    formatted_operations = [format_operations(operation) for operation in last_operations]

    # Ожидаемый результат
    expected_output = '\n\n'.join(formatted_operations)
    assert prepare_operations(test_data) == expected_output

import os
from utils import load_data, prepare_operations
from config import ROOT_DIR


def main():
    """
    Функция осуществляет загрузку данных о банковских операциях из файла JSON,
    используя функцию load_data из модуля utils.
    Затем данные обрабатываются функцией prepare_operations,
    чтобы получить отформатированную информацию о последних выполненных операциях.
    """
    DATA_PATH = os.path.join(ROOT_DIR, 'src', 'operations.json')
    operations = load_data(DATA_PATH)
    print(prepare_operations(operations))


if __name__ == "__main__":
    main()

from utils import load_data, prepare_operations


def main():
    """
    Функция осуществляет загрузку данных о банковских операциях из файла JSON,
    используя функцию load_data из модуля utils.
    Затем данные обрабатываются функцией prepare_operations,
    чтобы получить отформатированную информацию о последних выполненных операциях.
    """
    operations = load_data("operations.json")
    print(prepare_operations(operations))


if __name__ == "__main__":
    main()

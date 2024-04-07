import os
from utils import load_data, format_operations
from config import ROOT_DIR


def main():
    DATA_PATH = os.path.join(ROOT_DIR, 'src', 'operations.json')
    operations = load_data(DATA_PATH)
    print(format_operations(operations[0]))


if __name__ == "__main__":
    main()

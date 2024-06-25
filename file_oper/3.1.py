import random

def create_files():
    for i in range(1, 11):  # для создания десяти файлов реализован цикл с использованием f - строк
        with open((f'{i}.txt'), 'w') as fi:
            fi.write(f"{random.randint(1, 10)}\n")
            fi.write(f"{random.randint(1, 10)}\n")
            fi.write(f"{random.randint(1, 10)}")

create_files()

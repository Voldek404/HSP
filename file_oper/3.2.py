import random


# для проверки исключения сделан файл 11.txt

def file_ins(a, b):
    sum_1 = 0
    with open((f'{a}.txt'), 'r') as fi_1:
        for s1 in fi_1:
            s1 = s1.strip()
            if not s1:  # проверка на пустую строку
                pass
            try:
                sum_1 += int(s1)
            except ValueError:
                print(f"Ошибка преобразования строки в число в файле {a}")
                return False
    sum_2 = 0
    with open((f"{b}.txt"), 'r') as fi_2:
        for s2 in fi_2:
            s2 = s2.strip()
            if not s2:  # проверка на пустую строку
                pass
            try:
                sum_2 += int(s2)
            except ValueError:
                print(f"Ошибка преобразования строки в число в файле {b}")
                return False
    return sum_1 + sum_2


a = random.randint(1, 10)
b = random.randint(1, 10)
print("Первый номер файла -- ", a)
print("Второй  номер файла -- ", b)
print("Сумма шести чисел составляет -- ", file_ins(a, b))

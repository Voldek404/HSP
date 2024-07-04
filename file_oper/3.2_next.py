import random


# для проверки исключения сделан файл 11.txt

def file_ins(file_list):
    sum_1 = 0
    for names in file_list:
        with open((f'{names}.txt'), 'r') as fi:
            for s in fi:
                s = s.strip()
                if not s:  # проверка на пустую строку
                    pass
                try:
                    sum_1 += int(s)
                except ValueError:
                    print(f"Ошибка преобразования строки в число в файле {i}")
                    return False
    return sum_1


a = random.randint(1, 10)
b = random.randint(1, 10)
file_list =[a,b]

print("Первый номер файла -- ", a)
print("Второй  номер файла -- ", b)
print("Сумма шести чисел составляет -- ", file_ins(file_list))

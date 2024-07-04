import random


def file_ins(file_list: list[str]) -> int:
    sum_1 = 0
    for names in file_list:
        with open((f'{names}.txt'), 'r') as fi:
            for s in fi:
                try:
                    s = s.strip()
                    sum_1 += int(s)
                except Exception:
                    return [0, 1] #сигнализация ошибки
    return [sum_1,0]


a = random.randint(1, 10)
b = random.randint(1, 10)
file_list = [a,b]

print("Первый номер файла -- ", a)
print("Второй  номер файла -- ", b)
print("Общее количество золота составляет -- ", file_ins(file_list))

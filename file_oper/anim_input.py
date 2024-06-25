# программа для заполнения в готовый список имен параметров веса и частоты
import random

output = ''
with open('animals.txt', 'r') as anim:
    for line in anim:  # считывание текущего файла
        a = str(random.randint(10, 100))  # set up weight
        b = str(random.randint(16, 20000))  # set up fq
        output += (line.replace('\n', '') + ' ' + a + ' ' + b + '\n')
with open('animals.txt', 'w') as file:
    file.write(output)

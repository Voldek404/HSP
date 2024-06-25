for i in range(1, 51):
    if i % 5 == 0 and i % 3 == 0:
        print('*333*555*')
    elif i % 5 == 0:
        print('*555*')
    elif i % 3 == 0:
        print('*333*')
    else:
        print(i)

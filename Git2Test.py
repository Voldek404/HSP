def palindrom(x):
    x_rev = []
    for i in range(len(x), 0, -1):
        x_rev.append(x[i - 1])
    if x == x_rev:
        return True
    else:
        return False


x = list(str(input()))
print(palindrom(x))

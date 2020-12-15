def implication(a, b):
    if not a:
        return True
    return b

for A in range(1, 1000):
    flag = 1
    for x in range(1, 1000):
        if not implication(x % 19 != 0 or x % 15 != 0, x % A != 0):
            flag = 0
            break
    if flag:
        print(A)
        break
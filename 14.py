s = 16 ** 20 + 2 ** 30 - 32
counter = 0
while s > 0:
    if s % 4 == 3:
        counter += 1
    s //= 4
print(counter)

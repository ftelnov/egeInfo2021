# Поиск простых чисел на отрезке

def is_simple(x):
    for i in range(2, int(x ** 0.5) + 1):
        if x % i == 0:
            return False
    return True


print(list(filter(is_simple, range(4202865, 4202924))))

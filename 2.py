from itertools import product


def implication(a, b):
    if not a:
        return True
    return b


print(list(filter(lambda tup: implication(implication(tup[0], tup[1]), (not tup[0] and tup[1])), product([1, 0], repeat=3))))

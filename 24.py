# Пример числовой выжимки из буквенно-числового файла
import re

with open('24-1.txt') as file:
    data = list(map(int, re.findall(r'\d+', file.read())))
    print(max(filter(lambda x: all(map(lambda _x: int(_x) % 2 != 0, list(str(x)))), data)))

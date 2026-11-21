# https://kompege.ru/task?id=18941

from itertools import *
def f(N):
    m = []
    n = str(N)
    for i in range(1,4):
        m.append(int(n[0]) * int(n[i])) # записываем результаты произведения первой цифры с остальными в список
    s = sorted(m) # сортируем их по возрастанию
    r = str(s[1]) + str(s[2])
    return int(r)
for N in range(1000,10000):
    if f(N) == 5472:
        print(N)
        break

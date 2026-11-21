# https://kompege.ru/task?id=31219

from math import *
N = 10 + 510
cnt = 18982657
mem = 9379 * 1024**2
i = ceil(log2(N))
for len in range (1,1000):
    if ceil(i * len / 8) * cnt >= mem:
        print(len)
        break

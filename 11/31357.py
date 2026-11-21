# https://kompege.ru/task?id=31357

from math import *
N = 10 + 120
cnt = 12755226
mem = 5 * 1024 * 1024 * 1024
i = ceil(log2(N))
for len in range(1000,0,-1):
    if ceil(i * len / 8) * cnt <= mem:
        print(len)
        break

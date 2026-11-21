# https://kompege.ru/task?id=31149

from math import *
cnt = 1892412
len = 440
mem = 305726 * 1024
for i in range(1,100):
    if ceil(i * len / 8) * cnt >= mem:
        print(2**(i - 1) + 1)
        break

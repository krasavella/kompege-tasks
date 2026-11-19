from math import *
N = 16
i = ceil(log2(N))
cnt = 8192
memall = 4016 * 1024
mem1 = ceil(memall / cnt)
for len in range(10000,0,-1):
    if ceil((i * len + 13) / 8) <= mem1:
        print(len)
        break

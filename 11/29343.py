from math import *
len = 257
N = 4080 + 17
cnt = 8388608
i = ceil(log2(N))
mem1 = ceil(len * i / 8)
memall = mem1 * cnt
print(ceil(memall / (1024**2)))

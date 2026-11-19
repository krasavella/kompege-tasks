from math import *
N = 10 + 120
cnt = 12755226
mem = 5 * 1024 * 1024
i = log2(N)
for len in range(10000,0,-1):
    if (i * len / 8) * cnt <= mem:
        print(len)
        break

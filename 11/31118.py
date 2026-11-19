from math import *
len = 172
cnt = 187564
mem = 39 * 1024**2
for i in range(10000,0,-1):
    if ceil(i * len / 8) * cnt <= mem:
        print(2**i)

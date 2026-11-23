# https://kompege.ru/task?id=31123

from functools import lru_cache
@lru_cache(None)
def f(n):
    if n == 1:
        return n
    if n > 1:
        return n * f(n-1)

for n in range(1,3300):
    f(n)
print(((f(3238)//2) + f(3237))//f(3236))

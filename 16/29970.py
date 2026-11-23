# https://kompege.ru/task?id=29970

from functools import lru_cache

@lru_cache(None)
def g(n):
    if n <= 20:
        return n + 2
    else:
        return g(n - 3) + 1

def f(n):
    return 3 * g(n - 3) + 7

for n in range(1,40000):
    g(n)
print(f(37811))


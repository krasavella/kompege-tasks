# КОМПЕГЭ № 31123 — https://kompege.ru/task?id=31123
#
# Функция F задана для целого n рекуррентно: F(1) = 1, а при n > 1
# выполняется F(n) = n · F(n − 1).
# Вычислите (F(3238) / 2 + F(3237)) / F(3236).

from functools import lru_cache
import sys
sys.setrecursionlimit(50000)
@lru_cache(None)
def f(n):
    if n == 1:
        return n
    if n > 1:
        return n * f(n-1)
print(f(3238)//2 + f(3237)//f(3236))

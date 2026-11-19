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

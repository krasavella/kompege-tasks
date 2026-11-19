from functools import lru_cache
@lru_cache(None)
def f(a,b):
    if a > b: return 0
    if a == b: return 1
    s = bin(a)[2:]
    n = s.count('1')
    return f(a + 1,b) + f(a + n,b)
print(f(5,40))

# https://kompege.ru/task?id=31419

from functools import lru_cache
@lru_cache(None)
def f(a,b,k):
    if a > b: return 0
    if a == b and k == 3: return 1
    s = str(a)
    if s.count('1') >= 1: return f(a+1,b,k) + f(int(s.replace('1', '3')), b, k + 1)
    return f(a+1,b, k)
print(f(11,94,0))

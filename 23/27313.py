# https://kompege.ru/task?id=27313

from functools import lru_cache
@lru_cache(None)
def f(a,b,k):
    if a > b or a == 20 or a == 33: return 0
    if a == 15 or a == 26: k +=1
    if a == b: return k > 0
    return f(a + 3,b,k) + f(a + 4,b,k) + f(a * 2,b,k)
print(f(3,63,0))

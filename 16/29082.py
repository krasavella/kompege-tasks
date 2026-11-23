# https://kompege.ru/task?id=29082

from functools import lru_cache

@lru_cache(None)
def f(n):
    if n < 19:
        return 5
    else:
        return (n + 4) * f(n - 7)

for n in range(1,160000):
    f(n)

print((f(157163)//234 + f(157149)//533)//f(157142))

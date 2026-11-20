# КОМПЕГЭ № 27313 — https://kompege.ru/task?id=27313
#
# У исполнителя три команды: A прибавляет 3, B прибавляет 4,
# C умножает на 2. Программа — последовательность этих команд.
# Сколько программ переводят число 3 в 63 так, что на пути есть
# хотя бы одно из чисел 15 и 26, а числа 20 и 33 отсутствуют?

from functools import lru_cache
@lru_cache(None)
def f(a,b,k):
    if a > b or a == 20 or a == 33: return 0
    if a == 15 or a == 26: k +=1
    if a == b: return k > 0
    return f(a + 3,b,k) + f(a + 4,b,k) + f(a * 2,b,k)
print(f(3,63,0))

# https://kompege.ru/task?id=21243

def p(N):
    n = ''
    while N > 0:
        n = str(N % 5) + n
        N //= 5
    return n
def f(N):
    n = p(N)
    if int(sum(map(int, str(n)))) % 5 == 0:
        r = n.replace('0', '*').replace('1','0').replace('*', '1') + '14'    # сначала нули заменяем на *, чтобы не запороть все
    else:
        r = n[2:] + '33'
    return int(r, 5)
a = []
for N in range(1,1000):
    if f(N) > 370:
        a.append([f(N), N]) # тут в a добавляются связанные N и результат функции
a.sort() # ставятся в порядке возрастания
print(a[0][1])


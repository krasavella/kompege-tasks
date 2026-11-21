# https://kompege.ru/task?id=22267

def s(N):
    n = ''
    while N > 0:
        n = str(N % 7) + n
        N //= 7
    return n
def f(N):
    n = s(N)
    if n[-1] == '2':
        r = '21' + n.replace('3', '*').replace('1', '3').replace('*', '1')
    else:
        r = '1' + n[1:] + '36'
    return int(r, 7)
a = []
for N in range(1,1000):
    if f(N) < 744:
        a.append([-f(N),N]) # тут результат функции отрицателен, потому что надо найти минимальную N и максимальную f(N)
a.sort()
print(a[0][1]) # модуля нет, потому что мы выводим N, а не результат функции


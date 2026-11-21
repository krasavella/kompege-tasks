# https://kompege.ru/task?id=21473

def g(N):
    n = ''
    while N > 0:
        n = str(N % 3) + n
        N //= 3
    return n

def f(N):
    n = g(N)
    if sum(map(int, n)) % 4 == 0:
        r = '10' + n.replace('1', '*').replace('2', '1').replace('*', '2')
    else:
        r = n[0] + '02' + n[3:] + '20'
    return int(r, 3)

a = []
for N in range(1,100000):
    if f(N) > 302:
        a.append([f(N), -N])

a.sort()
print(abs(a[0][1]))


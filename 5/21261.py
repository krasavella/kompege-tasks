def g(N):
    n = ''
    while N > 0:
        n = str(N % 4) + n
        N //= 4
    return n

def f(N):
    n = g(N)
    if sum(map(int, n)) % 3 == 0:
        r = '32' + n.replace('0', '*').replace('2', '0').replace('*', '2')
    else:
        r = n[0] + '10' + n[3:] + '33'
    return int(r, 4)

a = []
for N in range(1,10000):
    if f(N) > 320:
        a.append([f(N), -N])
a.sort()
print(abs(a[0][1]))


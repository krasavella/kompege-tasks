def t(N):
    n = ''
    while N > 0:
        n = str(N % 3) + n
        N //= 3
    return n
def f(N):
    n = t(N)
    if N % 3 == 0:
        r = '1' + n + '02'
    else:
        r = n + t(N % 3 * 5)
    return int(r, 3)

for N in range(1,1000):
    if f(N) >= 177:
        print(N)
        break

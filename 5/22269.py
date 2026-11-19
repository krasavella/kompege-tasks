def g(N):
    n = ''
    while N > 0:
        n = str(N % 5) + n
        N //= 5
    return n

def f(N):
    n = g(N)
    if n[-1] == '0':
        r = '33' + n.replace('1', '*').replace('4', '1').replace('*', '4')
    else:
        r = '3' + n[1:] + '42'
    return int(r, 5)

a = []
for N in range(1,100000):
    if f(N) < 1922:
        a.append([-f(N),N])
a.sort()
print(a[0][1])

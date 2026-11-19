def g(N):
    n = ''
    while N > 0:
        n = str(N % 6) + n
        N //= 6
    return n

def f(N):
    n = g(N)
    if sum(map(int, n)) % 5 == 0:
        r = '11' + n.replace('0', '*').replace('3', '0').replace('*', '3')
    else:
        r = n[0] + '05' + n[3:] + '44'
    return int(r, 6)

a = []
for N in range(1,100000):
    if f(N) > 1500:
        a.append([f(N), -N])
a.sort()
print(abs(a[0][1]))

        

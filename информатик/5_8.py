from string import *

def g(N): # функция переводит в 12-ричную систему
    alf = digits + ascii_uppercase
    n = ''
    while N > 0:
        n = alf[N % 12] + n
        N //= 12
    return n

def f(N):
    n = g(N)
    if N % 4 == 0:
        r = '2' + n + '64'
    else:
        r = n + max(n)
    return int(r, 12)

a = []
for N in range(1,10000):
    if f(N) > 1799:
        a.append(f(N))
print(min(a))
        


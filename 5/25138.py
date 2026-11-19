def f(N):
    S = sum(map(int, str(N)))
    n = str(N).split()
    M = int(max(n)) + int(min(n))
    L = int(n[0])
    R = int(n[-1])
    p1 = S - L
    p2 = M - R
    a = []
    a.append(p1)
    a.append(p2)
    a = sorted(a)
    z = ''.join(str(a))
    return int(z)
for N in range(10000,100000):
    if f(N) == 222:
        print(N)


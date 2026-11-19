def f(N):
    n = [int(x) for x in str(N)]
    S = sum([int(x) for x in str(N)])
    M = max(n) + min(n)
    L = int(n[0])
    R = int(n[-1])
    p1 = S - L
    p2 = M - R
    if p1 >= p2:
        z = str(p2) + str(p1)
    else:
        z = str(p1) + str(p2)
    return int(z)
for N in range(10000,100000):
    if f(N) == 222:
        print(N)


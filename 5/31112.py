def f(N):
    n = bin(N)[2:]
    if N % 2 == 0:
        r = '11' + n + '11'
    else:
        r = '1' + n + '00'
    r = int(r, 2)
    return r
for N in range(10000,0,-1):
    if f(N) <= 113:
        print(f(N))
        break

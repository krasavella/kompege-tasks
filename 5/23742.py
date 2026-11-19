def f(N):
    n = bin(N)[2:]
    if N % 3 == 0:
        r = n + n[-3:0]
    else:
        r = n + bin(N % 3 * 3)[2:]
    return int(r, 2)

for N in range(1,10000):
    if f(N) >= 200:
        print(N)
        break

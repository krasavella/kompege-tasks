def f(N):
    n = bin(N)[2:]
    if N % 2 == 0:
        r = n.replace('0', '1')
    else:
        r = n[0] + n[1:].replace('1', '00')
    return int(r, 2)

a = []
for N in range(1,1000000):
    if f(N) <= 600:
        a.append([f(N), N])
a.sort()
print(a[-1][1])

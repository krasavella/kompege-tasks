def sl(N):
    n = str(N)
    n1 = int(n[0]) + int(n[1])
    n2 = int(n[0]) * int(n[1])
    if n2 > n1:
        r = str(n1) + str(n2)
        return int(r)
    else:
        r = str(n2) + str(n1)
        return int(r)
for N in range(10,100):
    if sl(N) == 710:
        print(N)
        break


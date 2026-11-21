# https://kompege.ru/task?id=25138

def f(N):
    n = str(N)
    S = sum(map(int, str(N)))    # я так записал сумму цифр числа N
    M = int(max(n)) + int(min(n))
    L = int(n[0])
    R = int(n[-1])
    p1 = S - L
    p2 = M - R
    if p1 >= p2:
        z = str(p2) + str(p1)
    else:
        z = str(p1) + str(p2)
    return int(z)
for N in range(100000,9999,-1):
    if f(N) == 222:
        print(N)
        break


# https://kompege.ru/task?id=20883

def p(N):
    n = ''
    while N > 0:
        n = str(N % 5) + n
        N //= 5    # просто сокращенная запись
    return n
def f(N):
    n = p(N)
    if len(n) % 2 == 0:
        r = n[len(n) // 2:] + n[:len(n) // 2]
    else:
        r = n + str(N % 5)
        r = r[len(r) // 2:] + r[:len(r) // 2]
    return int(r, 5)

for N in range(1,1000):
    if f(N) > 50:
        print(N)
        break



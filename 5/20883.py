def p(N):
    n = ''
    while N > 0:
        n = str(N % 5) + n
        N //= 5
    return n
def f(N):
    n = p(N)


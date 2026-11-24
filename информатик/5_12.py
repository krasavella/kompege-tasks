def f(N):
    a = [int(i) for i in str(N)]
    s = sum(a)
    m = max(a)
    n = min(a)
    p = 1
    for i in a:
        if i != 0:
            p *= i
    b1 = s - m - n
    b2 = p - (2 * s)
    if b1 > b2:
        r = str(b1) + str(b2)
    else:
        r = str(b2) + str(b1)
    return r

print(max([a for a in range(100000,1000000) if f(a) == '26714']))

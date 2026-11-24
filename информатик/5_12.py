def f(a):
    a1 = str(a)
    s = int(sum(map(int, a1)))
    m = int(max(a1))
    n = int(min(a1))
    p = 1
    for i in a1:
        if i:
            p *= int(i)
    b1 = s - m - n
    b2 = p - (2 * s)
    if b1 > b2:
        r = str(b1) + str(b2)
    else:
        r = str(b2) + str(b1)
    return r

print(max([a for a in range(100000,1000000) if f(a) == '26714']))

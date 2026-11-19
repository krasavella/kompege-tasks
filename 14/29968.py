for x in range(3000, 0, -1):
    k = 0
    a = 9 * 11**210 + 8 * 11**150 - x
    while a > 0:
        if a % 11 == 0:
            k += 1
        a = a // 11
    if k == 60:
        print(x)
        break

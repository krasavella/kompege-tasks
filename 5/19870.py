# https://kompege.ru/task?id=19870

def tr(N):
    if N == 0:
        return '0'
    n = ''
    while N != 0:
        n = str(N % 4) + n
        N //= 4    # просто сокращенная запись
    return n
        
def f(N):
    n = tr(N)
    if N % 2 == 0:
        r = '12' + n + tr(int(n[-1],4) * 3)    # берется результат перевода последней цифры из n в десятичную систему и обратно в четверичную и умножается на 3
    else:
        r = '13' + n + '21'
    return int(r, 4)
for N in range(0,1000):
    if f(N) > 50:
        print(f(N))
        break

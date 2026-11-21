# https://kompege.ru/task?id=23742

def f(N):
    n = bin(N)[2:]
    if N % 3 == 0:
        r = n + n[-3:] # прибавляем три последние цифры
    else:
        r = n + bin(N % 3 * 3)[2:] # советую ставить скобки
    return int(r, 2)

for N in range(1,10000):
    if f(N) >= 200:
        print(N)
        break

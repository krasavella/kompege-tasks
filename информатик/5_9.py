def f(N):
    n = str(N)
    x = []
    # a = int(n[0]) + int(n[1])
    # b = int(n[1]) + int(n[2])
    # c = int(n[2]) + int(n[3])
    # d = int(n[3]) + int(n[4])
    for i in range(len(n) - 1): # этот страшный цикл позволяет посчитать сумму последующих чисел (1 и 2, 2 и 3 и тд) в любом числе
        x.append(int(n[i]) + int(n[i+1])) 
    x.remove(max(x)) # удаление максимального значения
    x.remove(min(x)) # удаление минимального значения
    if x[0] > x[1]:
        r = str(x[1]) + str(x[0])
    else:
        r = str(x[0]) + str(x[1])
    return int(r)

for N in range(10000,100000):
    if f(N) == 1015:
        print(N)
        break


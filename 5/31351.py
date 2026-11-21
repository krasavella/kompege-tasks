# https://kompege.ru/task?id=31351
       
def f(N):
    n = bin(N)[2:]
    if int(n.count('1')) % 2 == 0:
        r = '10' + n[2:] + '0'
    else:
        r = '11' + n[2:] + '1'
    return int(r, 2)
for N in range (1,10000):
    if f(N) >= 16:
        print(N)
        break


# https://kompege.ru/task?id=22271

def f(N):
    n = oct(N)[2:]
    if n[0] == '5':
        r = n.replace('2', '1')
        r = '11' + n.replace('1', '2') # еще не знал про замену со *. ответ тоже был верный
    else:
        
        r = '2' + n[1:] + '10'
    return int(r, 8)
for N in range(10000,0,-1):
    if f(N) < 1354:
        print(N, f(N))
# я тут еще про способ со списком не знал, так что выбирал руками


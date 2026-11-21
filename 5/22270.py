# https://kompege.ru/task?id=22270

def tr(N):
    n = ''
    while N > 0:
        n = str(N % 4) + n
        N //= 4    # просто сокращенная запись
    return n
        
def f(N):
    n = tr(N)
    if n[0] == '3':
        r = n.replace('1','3')    # первое задание, где я встретился с заменой. я не знаю работает ли это, но ответ вроде был верный
        r = n.replace('3', '1') + '21'
    else:
        r = '1' + n[1:] + '12'
    return int(r, 4)
for N in range (10000,0,-1):
    if f(N) < 598:
        print(N)
        break


# https://kompege.ru/task?id=20883

def p(N):
    n = ''
    while N > 0:
        n = str(N % 5) + n
        N //= 5    # просто сокращенная запись
    return n
def f(N):
    n = p(N)
    # С.Л.О.Ж.Н.О. 
    # там есть какая-то запись, но мне лень ее разбирать


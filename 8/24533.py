# https://kompege.ru/task?id=24533

from itertools import product
m = []
k = 0
sm = 0
for x in product(sorted('НЕАТОК'), repeat=7):
    s = ''.join(x)
    k += 1
    if k % 2 != 0 and s not in 'А' and s.count('К') == 2 and s.count('О') == 2 and s.count('Е') == 1 and s.count('Н') == 1 and s.count('Т') == 1:
        print(k)

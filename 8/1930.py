from itertools import permutations
k = 0
for x in permutations('АПЕЛЬСИН', r = 7):
    s = ''.join(x)
    for y in 'ПЛСН':
        s = s.replace(y, 'С') # заменяем согласные на С для удобства
    if ('СЬС' in s) or ('Ь' not in s):
        k += 1
print(k)

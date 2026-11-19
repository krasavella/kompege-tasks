from string import *
def f(ishod):
    n = 0
    for c in ishod:
        n = n * 40 + int(c, 36)
    return n
for x in (digits + ascii_uppercase + ascii_lowercase)[:40]:
    a = f(f'871{x}291') + f(f'366{x}631') + f(f'973{x}618')
    if a % 39 == 0:
        print(x, a // 13)

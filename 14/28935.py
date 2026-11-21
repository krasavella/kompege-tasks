# https://kompege.ru/task?id=28935

from string import *
for x in (digits + ascii_uppercase)[:23]:
    a = int(f'761{x}035', 23) + int(f'338{x}932', 23)
    if a % 22 == 0:
        print(x, a // 22)

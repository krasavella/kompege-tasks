# конвертация айпи в бинарник, есть несколько способов
# ip_bin = f'{int(ip):032b}'
# ip_bin = bin(int(ip))[2:].zfill(32)

# еще нюансы про айпи
# наибольший адрес - [-2]
# наименьший - [1]
#
# как сразу получить айпишник без точек:
# print(str(net[]).join('.'))

# универсальные функции для конвертации 1) из любой в дес 2) из дес. в любую
# def f(a, base):
#     n = 0
#     alf = digits + ascii_uppercase + ascii_lowercase
#     for c in a:
#         n = n * base + alf.index(c)
#     return n
#
# def g(n, base):
#     alf = digits + ascii_uppercase + ascii_lowercase
#     s = ''
#     while n > 0:
#         s = alf[n % base] + s
#         n = n // base
#     return s
# print(f('G20', 37))

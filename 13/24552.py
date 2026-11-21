# https://kompege.ru/task?id=24552

from ipaddress import *
net = ip_network('202.71.92.91/255.255.192.0', 0)
for ip in net.hosts():
    i = str(ip).split('.')
    if sum(int(x) % 2 != 0 for x in i) == 2: # идет перебор октетов чтобы проверить их нечетность
        print(ip)

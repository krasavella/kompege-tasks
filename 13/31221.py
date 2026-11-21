# https://kompege.ru/task?id=31221

from ipaddress import *
nw = ip_network('64.237.228.143/255.255.248.0', 0)
print(nw[0])
print(sum(map(int, str(nw[0]).split('.'))))

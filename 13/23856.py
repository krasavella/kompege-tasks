from ipaddress import *
net = ip_network('172.95.116.174/255.255.192.0',0)
for ip in net.hosts():
    if f'{int(ip):032b}'.count('1') % 5 == 0:
        print(ip)
        break
print(sum(map(int, str(ip).split('.'))))


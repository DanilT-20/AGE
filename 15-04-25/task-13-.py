from ipaddress import ip_network
from itertools import count
count = 0
for i in ip_network('172.16.192.0/255.255.192.0'):
    i = f'{int(i):032b}'
    if i.count('1') != 5:
        count += 1
print(count)
from ipaddress import ip_network
count = 0
net = ip_network('102.141.0.0/255.255.192.0')
for i in net:
    i = f'{int(i):032b}'
    if i.count('1')%7 == 0 and i[-4:] == '1011':
        count += 1
print(count)
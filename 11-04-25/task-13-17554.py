from ipaddress import ip_network

count = 0
for i in ip_network('112.160.0.0/255.240.0.0'):
    i = f'{int(i):032b}'
    if i.count('1') %3!=0:
        count += 1
print(count)
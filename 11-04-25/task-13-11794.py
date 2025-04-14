from ipaddress import ip_network
for n in range(256):
    net = ip_network(f'223.167.{n}.167/26',False)
    count = 0
    for i in net:
        i = f'{int(i):032b}'
        if i[:16].count('0') <= i[16:].count('0'):
            count += 1
    if count == len(list(net)):
        print(n)
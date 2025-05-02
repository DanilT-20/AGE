from ipaddress import ip_network
for a in range(16, 25):
    net = ip_network(f'238.51.1.202/{a}', False)
    for i in net:
        i = f'{int(i):032b}'
        if not(i[:16].count('1') >= i[16:].count('1')):
            break
    else:
        print(net.netmask)
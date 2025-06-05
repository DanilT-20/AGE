from ipaddress import ip_network, ip_address
for i in range(256):
    net = ip_network(f'192.214.{i}.184/255.255.255.224', False)
    count = 0
    for n in net:
        n = f'{int(i):032b}'
        count += n.count('1')
    if count > 15:
        print(i)

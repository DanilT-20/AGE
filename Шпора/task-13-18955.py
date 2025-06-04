from ipaddress import ip_network, ip_address
ip1 = ip_address('200.154.190.12')
ip2 = ip_address('200.154.184.0')
for A in range(10, 31)[::-1]:
    net1 = ip_network(f'{ip1}/{A}', False)
    net2 = ip_network(f'{ip2}/{A}', False)
    if net1 == net2:
        if ip1 not in (net1.network_address, net1.broadcast_address):
            if ip2 not in (net2.broadcast_address, net2.network_address):
                print(A)
                break


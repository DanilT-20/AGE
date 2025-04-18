from ipaddress import ip_network, ip_address
ip1 = ip_address('121.171.5.70')
ip2 = ip_address('121.171.5.107')
for i in range(33):
    net1 = ip_network(f'{ip1}/{i}', False)
    net2 = ip_network(f'{ip2}/{i}', False)
    if net1.network_address == net2.network_address:
        if ip1 not in (net1.broadcast_address, net1.network_address):
            if ip2 not in (net2.broadcast_address, net2.network_address):
                print(net1.num_addresses)
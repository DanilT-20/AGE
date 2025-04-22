from ipaddress import ip_network, ip_address
count = 0
net_ip = ip_address('218.48.192.0')
for mask in range(16, 25):
    net = ip_network(f'218.48.192.0/{mask}', False)
    if net.num_addresses >= 502 and net_ip  in net:
        count += 1
print(count)

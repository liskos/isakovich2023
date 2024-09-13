import ipaddress


ip = ipaddress.ip_address('115.12.69.38')
for i in range(1, 32):
    net = ipaddress.ip_network(f'115.12.64.0/{i}', 0)
    if ip in net:
        print(net, net.netmask)
import ipaddress


ip = ipaddress.ip_address('218.217.212.15')
for i in range(1, 32):
    net = ipaddress.ip_network(f'218.217.192.0/{i}', 0)
    if ip in net:
        print(net, net.netmask)
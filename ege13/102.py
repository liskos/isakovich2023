import ipaddress


ip = ipaddress.ip_address('120.120.120.35')
for i in range(1, 32):
    net = ipaddress.ip_network(f'120.120.120.0/{i}', 0)
    if ip in net:
        print(net, net.netmask)
#19
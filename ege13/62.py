import ipaddress


ip = ipaddress.ip_address('158.198.228.220')
for i in range(1, 32):
    net = ipaddress.ip_network(f'158.198.128.0/{i}',0)
    if ip in net:
        print(net, net.netmask)
#128
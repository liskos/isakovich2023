import ipaddress


ip = ipaddress.ip_address('153.209.31.240')
for i in range(1, 32):
    net = ipaddress.ip_network(f'153.209.28.0/{i}',0)
    if ip in net:
        print(net, net.netmask)
#252
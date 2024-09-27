import ipaddress


ip = ipaddress.ip_address('248.228.60.240')
for i in range(1, 32):
    net = ipaddress.ip_network(f'248.228.56.0/{i}',0)
    if ip in net:
        print(net, net.netmask)
#248
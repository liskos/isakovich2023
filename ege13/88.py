import ipaddress


ip = ipaddress.ip_address('63.132.140.28')
for i in range(1, 32):
    net = ipaddress.ip_network(f'63.132.140.0/{i}', 0)
    if ip in net:
        print(net, net.netmask)
#27
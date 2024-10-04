import ipaddress


ip = ipaddress.ip_address('148.195.140.28')
for i in range(1, 32):
    net = ipaddress.ip_network(f'148.195.140.0/{i}', 0)
    if ip in net:
        print(net, net.netmask)
#20
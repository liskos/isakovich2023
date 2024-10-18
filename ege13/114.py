import ipaddress


ip = ipaddress.ip_address('132.47.160.46')
for i in range(1, 32):
    net = ipaddress.ip_network(f'132.47.160.0/{i}', 0)
    if ip in net:
        print(net, net.netmask)
#8
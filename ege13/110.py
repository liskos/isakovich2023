import ipaddress


ip = ipaddress.ip_address('18.168.250.32')
for i in range(1, 32):
    net = ipaddress.ip_network(f'18.168.240.0/{i}', 0)
    if ip in net:
        print(net, net.netmask)
#1
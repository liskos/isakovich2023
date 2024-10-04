import ipaddress


ip = ipaddress.ip_address('192.168.104.15')
for i in range(1, 32):
    net = ipaddress.ip_network(f'192.168.104.0/{i}', 0)
    if ip in net:
        print(net, net.netmask)
#11
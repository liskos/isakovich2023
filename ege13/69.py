import ipaddress


ip = ipaddress.ip_address('217.138.127.144')
for i in range(1, 32):
    net = ipaddress.ip_network(f'217.138.64.0/{i}',0)
    if ip in net:
        print(net, net.netmask)
#192

import ipaddress


ip = ipaddress.ip_address('148.228.120.242')
for i in range(1, 32):
    net = ipaddress.ip_network(f'148.228.112.0/{i}',0)
    if ip in net:
        print(net, net.netmask)
#240
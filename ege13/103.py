import ipaddress


ip = ipaddress.ip_address('214.224.120.40')
for i in range(1, 32):
    net = ipaddress.ip_network(f'214.224.120.0/{i}', 0)
    if ip in net:
        print(net, net.netmask)
#26
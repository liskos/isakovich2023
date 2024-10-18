import ipaddress


ip = ipaddress.ip_address('154.112.144.160')
for i in range(1, 32):
    net = ipaddress.ip_network(f'154.112.144.0/{i}', 0)
    if ip in net:
        print(net, net.netmask)
#5
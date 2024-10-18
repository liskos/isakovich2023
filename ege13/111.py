import ipaddress


ip = ipaddress.ip_address('138.75.241.160')
for i in range(1, 32):
    net = ipaddress.ip_network(f'138.75.240.0/{i}', 0)
    if ip in net:
        print(net, net.netmask)
#4
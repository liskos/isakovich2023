import ipaddress


ip = ipaddress.ip_address('131.149.64.13')
for i in range(1, 32):
    net = ipaddress.ip_network(f'131.149.64.0/{i}', 0)
    if ip in net:
        print(net, net.netmask)
#11
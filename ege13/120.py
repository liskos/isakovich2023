import ipaddress


ip = ipaddress.ip_address('199.92.65.189')
for i in range(1, 32):
    net = ipaddress.ip_network(f'199.92.64.0/{i}', 0)
    if ip in net:
        print(net, net.netmask)
#6
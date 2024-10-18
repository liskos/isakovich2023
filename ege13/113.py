import ipaddress


ip = ipaddress.ip_address('169.97.112.115')
for i in range(1, 32):
    net = ipaddress.ip_network(f'169.97.112.0/{i}', 0)
    if ip in net:
        print(net, net.netmask)
#6
import ipaddress


ip = ipaddress.ip_address('156.32.140.138')
for i in range(1, 32):
    net = ipaddress.ip_network(f'156.32.128.0/{i}', 0)
    if ip in net:
        print(net, net.netmask)
#20
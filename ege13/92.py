import ipaddress


ip = ipaddress.ip_address('142.198.113.106')
for i in range(1, 32):
    net = ipaddress.ip_network(f'142.198.112.0/{i}', 0)
    if ip in net:
        print(net, net.netmask)
#23
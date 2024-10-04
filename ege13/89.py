import ipaddress


ip = ipaddress.ip_address('118.105.136.60')
for i in range(1, 32):
    net = ipaddress.ip_network(f'118.105.136.0/{i}', 0)
    if ip in net:
        print(net, net.netmask)
#21
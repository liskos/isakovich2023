import ipaddress

ip = ipaddress.ip_address('90.155.69.100')
for i in range(15, 32):
    net = ipaddress.ip_network(f'90.155.69.0/{i}', 0)
    if ip in list(net)[1:-1]:
        print(net, net.netmask)
#8
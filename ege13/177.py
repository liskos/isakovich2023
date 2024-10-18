import ipaddress

ip = ipaddress.ip_address('90.155.69.100')
for i in range(1, 32):
    net = ipaddress.ip_network(f'90.155.69.0/{i}', 0)
    print(net, net.netmask)
#8
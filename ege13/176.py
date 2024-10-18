import ipaddress

ip = ipaddress.ip_address('180.2.252.76')
for i in range(1, 32):
    net = ipaddress.ip_network(f'180.2.224.0/{i}', 0)
    print(net, net.netmask)
#224
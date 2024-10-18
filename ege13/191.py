import ipaddress

ip = ipaddress.ip_address('111.7.92.52')

for i in range(1, 32):
    net = ipaddress.ip_network(f'111.7.92.32/{i}', 0)
    if ip in net:
        print(net, net.netmask)
#224
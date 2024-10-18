import ipaddress

ip = ipaddress.ip_address('92.52.42.52')

for i in range(1, 32):
    net = ipaddress.ip_network(f'92.52.42.0/{i}', 0)
    if ip in net:
        print(net, net.netmask)
#192
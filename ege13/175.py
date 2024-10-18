import ipaddress

ip = ipaddress.ip_address('134.73.209.97')
for i in range(1, 32):
    net = ipaddress.ip_network(f'134.73.192.0/{i}', 0)
    print(net, net.netmask)
#192
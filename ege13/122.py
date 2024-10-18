import ipaddress


ip = ipaddress.ip_address('106.113.64.105')
for i in range(1, 32):
    net = ipaddress.ip_network(f'106.113.64.0/{i}', 0)
    if ip in net:
        print(net, net.netmask)
#8
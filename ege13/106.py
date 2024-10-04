import ipaddress


ip = ipaddress.ip_address('212.168.104.5')
for i in range(1, 32):
    net = ipaddress.ip_network(f'212.168.104.0/{i}', 0)
    if ip in net:
        print(net, net.netmask.__format__('b').count('0'))
#3
import ipaddress


ip = ipaddress.ip_address('125.181.67.15')
for i in range(1, 32):
    net = ipaddress.ip_network(f'125.181.64.0/{i}', 0)
    if ip in net:
        print(net, net.netmask.__format__('b').count('0'))
#14
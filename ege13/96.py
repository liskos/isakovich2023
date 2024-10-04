import ipaddress


ip = ipaddress.ip_address('204.108.112.142')
for i in range(1, 32):
    net = ipaddress.ip_network(f'204.108.64.0/{i}', 0)
    if ip in net:
        print(net, net.netmask.__format__('b').count('0'))
#14
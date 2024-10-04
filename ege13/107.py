import ipaddress


ip = ipaddress.ip_address('221.117.97.115')
for i in range(1, 32):
    net = ipaddress.ip_network(f'221.117.96.0/{i}', 0)
    if ip in net:
        print(net, net.netmask.__format__('b').count('0'))
#9
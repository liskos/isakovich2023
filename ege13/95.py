import ipaddress


ip = ipaddress.ip_address('241.185.253.57')
for i in range(1, 32):
    net = ipaddress.ip_network(f'241.185.252.0/{i}', 0)
    if ip in net:
        print(net, net.netmask.__format__('b').count('0'))
#10
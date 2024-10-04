import ipaddress


ip = ipaddress.ip_address('193.138.70.47')
for i in range(1, 32):
    net = ipaddress.ip_network(f'193.138.64.0/{i}', 0)
    if ip in net:
        print(net, net.netmask)
#21
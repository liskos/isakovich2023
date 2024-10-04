import ipaddress


ip = ipaddress.ip_address('203.155.64.98')
for i in range(1, 32):
    net = ipaddress.ip_network(f'203.155.64.0/{i}', 0)
    if ip in net:
        print(net, net.netmask)
#25
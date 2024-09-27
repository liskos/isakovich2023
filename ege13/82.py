import ipaddress


ip = ipaddress.ip_address('15.51.208.15')
for i in range(1, 32):
    net = ipaddress.ip_network(f'15.51.192.0/{i}',0)
    if ip in net:
        print(net, net.netmask)
#224

import ipaddress


ip = ipaddress.ip_address('161.158.136.231')
for i in range(1, 32):
    net = ipaddress.ip_network(f'161.158.138.65/{i}',0)
    if ip in net:
        print(net, net.netmask)
#252

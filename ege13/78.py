import ipaddress


ip = ipaddress.ip_address('61.58.73.42')
for i in range(1, 32):
    net = ipaddress.ip_network(f'61.58.75.136/{i}',0)
    if ip in net:
        print(net, net.netmask)
#252

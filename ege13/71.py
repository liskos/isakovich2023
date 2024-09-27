import ipaddress


ip = ipaddress.ip_address('152.217.69.70')
for i in range(1, 32):
    net = ipaddress.ip_network(f'152.217.125.80/{i}',0)
    if ip in net:
        print(net, net.netmask)
#192

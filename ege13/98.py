import ipaddress


ip = ipaddress.ip_address('154.28.80.25')
for i in range(1, 32):
    net = ipaddress.ip_network(f'154.28.90.25/{i}', 0)
    if ip in net:
        print(net, net.netmask)
#
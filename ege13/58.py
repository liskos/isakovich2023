import ipaddress


ip = ipaddress.ip_address('134.92.108.145')
for i in range(1, 32):
    net = ipaddress.ip_network(f'134.92.104.0/{i}',0)
    if ip in net:
        print(net, net.netmask)
#248
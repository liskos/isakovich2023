import ipaddress


ip = ipaddress.ip_address('159.152.66.19')
for i in range(1, 32):
    net = ipaddress.ip_network(f'159.152.64.0/{i}', 0)
    if ip in net:
        print(net, net.netmask)
#5
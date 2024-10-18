import ipaddress


ip = ipaddress.ip_address('76.155.48.2')
for i in range(1, 32):
    net = ipaddress.ip_network(f'76.155.48.0/{i}', 0)
    if ip in net:
        print(net, net.netmask)
#11
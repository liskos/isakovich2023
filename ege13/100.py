import ipaddress


ip = ipaddress.ip_address('215.118.70.47')
for i in range(1, 32):
    net = ipaddress.ip_network(f'215.118.64.0/{i}', 0)
    if ip in net:
        print(net, net.netmask)
#18
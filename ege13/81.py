import ipaddress


ip = ipaddress.ip_address('215.181.200.27')
for i in range(1, 32):
    net = ipaddress.ip_network(f'215.181.192.0/{i}',0)
    if ip in net:
        print(net, net.netmask)
#240
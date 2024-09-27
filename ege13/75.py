import ipaddress


ip = ipaddress.ip_address('215.171.155.54')
for i in range(1, 32):
    net = ipaddress.ip_network(f'215.171.145.37/{i}',0)
    if ip in net:
        print(net, net.netmask)
#240

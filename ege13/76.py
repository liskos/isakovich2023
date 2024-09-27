import ipaddress


ip = ipaddress.ip_address('211.115.61.154')
for i in range(1, 32):
    net = ipaddress.ip_network(f'211.115.59.137/{i}',0)
    if ip in net:
        print(net, net.netmask)
#248

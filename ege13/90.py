import ipaddress


ip = ipaddress.ip_address('163.232.136.60')
for i in range(1, 32):
    net = ipaddress.ip_network(f'163.232.136.0/{i}', 0)
    if ip in net:
        print(net, net.netmask)
#26
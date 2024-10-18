import ipaddress


ip = ipaddress.ip_address('149.112.71.192')
for i in range(1, 32):
    net = ipaddress.ip_network(f'149.112.64.0/{i}', 0)
    if ip in net:
        print(net, net.netmask)
#4
import ipaddress
ip = ipaddress.ip_address('118.187.59.255')
for i in range(1, 32):
    net = ipaddress.ip_network(f'118.187.65.115/{i}', 0)
    if ip in net:
        print(net)
#17
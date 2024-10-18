import ipaddress
ip = ipaddress.ip_address('193.175.175.231')
for i in range(1, 32):
    net = ipaddress.ip_network(f'193.175.176.118/{i}', 0)
    if ip in net:
        print(net)
#160
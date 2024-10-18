import ipaddress
ip = ipaddress.ip_address('132.46.175.26')
for i in range(1, 32):
    net = ipaddress.ip_network(f'132.46.170.130/{i}', 0)
    if ip in net:
        print(net)
#21
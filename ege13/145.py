import ipaddress
ip = ipaddress.ip_address('198.75.95.31')
for i in range(1, 32):
    net = ipaddress.ip_network(f'198.75.96.13/{i}', 0)
    if ip in net:
        print(net)
#18
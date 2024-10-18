import ipaddress
k = 0
ip = ipaddress.ip_address('151.168.147.193')
for i in range(15, 32):
    net = ipaddress.ip_network(f'151.168.147.128/{i}', 0)
    if ip in list(net)[1:-1]:
        print(net)

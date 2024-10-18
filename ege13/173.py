import ipaddress
k = 0
ip = ipaddress.ip_address('190.120.251.78')
for i in range(15, 32):
    net = ipaddress.ip_network(f'190.120.251.0/{i}', 0)
    if ip in list(net)[1:-1]:
        print(net)

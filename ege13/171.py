import ipaddress
k = 0
ip = ipaddress.ip_address('229.117.114.172')
for i in range(10, 32):
    net = ipaddress.ip_network(f'229.117.112.0/{i}', 0)
    if ip in list(net)[1:-1]:
        print(net)

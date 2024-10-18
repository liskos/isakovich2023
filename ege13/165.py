import ipaddress
k = 0
for i in range(1, 32):
    net = ipaddress.ip_network(f'255.255.128.0/{i}', 0)
    print(net)


import ipaddress

ip = ipaddress.ip_address('151.168.147.193')
for i in range(1, 32):
    net = ipaddress.ip_network(f'151.168.147.128/{i}', 0)
    print(net)
#31
import ipaddress

ip = ipaddress.ip_address('190.120.251.78')
for i in range(1, 32):
    net = ipaddress.ip_network(f'190.120.251.0/{i}', 0)
    print(net)
#1
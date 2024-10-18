import ipaddress
ip = ipaddress.ip_address('108.133.75.91')
for i in range(1, 32):
    net = ipaddress.ip_network(f'108.133.75.64/{i}', 0)
    if ip in net:
        print(net)
print(2 ** 5)
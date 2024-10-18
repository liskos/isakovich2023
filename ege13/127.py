import ipaddress
ip = ipaddress.ip_address('111.81.200.27')
for i in range(1, 32):
    net = ipaddress.ip_network(f'111.81.192.0/{i}', 0)
    if ip in net:
        print(net)
print(2 ** 12)
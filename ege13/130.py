import ipaddress
ip = ipaddress.ip_address('156.133.216.35')
for i in range(1, 32):
    net = ipaddress.ip_network(f'156.133.216.0/{i}', 0)
    if ip in net:
        print(net)
print(2 ** 11)
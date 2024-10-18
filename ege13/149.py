import ipaddress
ip = ipaddress.ip_address('112.74.161.2')
for i in range(1, 32):
    net = ipaddress.ip_network(f'112.74.98.15/{i}', 0)
    if ip in net:
        print(net)
#0
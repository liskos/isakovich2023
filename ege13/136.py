import ipaddress
ip = ipaddress.ip_address('45.218.13.76')
for i in range(1, 32):
    net = ipaddress.ip_network(f'45.218.13.55/{i}', 0)
    if ip in net:
        print(net)
#24
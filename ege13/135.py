import ipaddress
ip = ipaddress.ip_address('151.172.115.121')
for i in range(1, 32):
    net = ipaddress.ip_network(f'151.172.115.156/{i}', 0)
    if ip in net:
        print(net)
#24
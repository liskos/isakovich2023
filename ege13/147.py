import ipaddress
ip = ipaddress.ip_address('191.131.175.201')
for i in range(1, 32):
    net = ipaddress.ip_network(f'191.131.160.170/{i}', 0)
    if ip in net:
        print(net)
#160
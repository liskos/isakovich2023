import ipaddress
ip = ipaddress.ip_address('45.214.123.173')
for i in range(1, 32):
    net = ipaddress.ip_network(f'45.214.123.131/{i}', 0)
    if ip in net:
        print(net)
#26
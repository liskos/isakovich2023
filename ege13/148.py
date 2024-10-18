import ipaddress
ip = ipaddress.ip_address('123.56.161.21')
for i in range(1, 32):
    net = ipaddress.ip_network(f'123.56.209.10/{i}', 0)
    if ip in net:
        print(net)
#128
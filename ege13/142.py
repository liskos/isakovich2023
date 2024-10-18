import ipaddress
ip = ipaddress.ip_address('143.175.103.191')
for i in range(1, 32):
    net = ipaddress.ip_network(f'143.175.79.156/{i}', 0)
    if ip in net:
        print(net)
#18
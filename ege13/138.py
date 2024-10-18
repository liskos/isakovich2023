import ipaddress
ip = ipaddress.ip_address('157.127.182.76')
for i in range(1, 32):
    net = ipaddress.ip_network(f'157.127.190.80/{i}', 0)
    if ip in net:
        print(net)
#20
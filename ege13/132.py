import ipaddress
ip = ipaddress.ip_address('112.117.107.70')
for i in range(1, 32):
    net = ipaddress.ip_network(f'112.117.121.80/{i}', 0)
    if ip in net:
        print(net)
print(2 ** 13)
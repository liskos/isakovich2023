import ipaddress
ip = ipaddress.ip_address('121.171.5.70')
for i in range(1, 32):
    net = ipaddress.ip_network(f'121.171.5.107/{i}', 0)
    if ip in net:
        print(net)
print(2 ** 6)
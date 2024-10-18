import ipaddress

ip = ipaddress.ip_address('115.53.128.88')
for i in range(1, 32):
    net = ipaddress.ip_network(f'115.53.128.0/{i}', 0)
    if ip in net and 2 ** (32-i)-2 >= 1000:
        print(net, 2 ** (32-i)-2)
#6
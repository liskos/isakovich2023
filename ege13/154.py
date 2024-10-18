import ipaddress

ip = ipaddress.ip_address('125.28.160.73')
for i in range(1, 32):
    net = ipaddress.ip_network(f'125.28.160.0/{i}', 0)
    if ip in net and 2 ** (32-i)-2 >= 500:
        print(net, 2 ** (32-i)-2)
#5
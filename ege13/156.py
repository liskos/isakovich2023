import ipaddress

ip = ipaddress.ip_address('188.214.176.25')
for i in range(1, 32):
    net = ipaddress.ip_network(f'188.214.176.0/{i}', 0)
    if ip in net and 2 ** (32-i)-2 >= 100:
        print(net, 2 ** (32-i)-2)
#6
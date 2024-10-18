import ipaddress

ip = ipaddress.ip_address('111.3.161.27')
for i in range(1, 32):
    net = ipaddress.ip_network(f'111.3.160.0/{i}', 0)
    if ip in net and 2 ** (32-i)-2 >= 2000:
        print(net, 2 ** (32-i)-2)
#3
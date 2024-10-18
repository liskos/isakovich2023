import ipaddress

ip = ipaddress.ip_address('175.122.80.13')
for i in range(1, 32):
    net = ipaddress.ip_network(f'175.122.80.0/{i}', 0)
    if ip in net and 2 ** (32-i)-2 >= 60:
        print(net, 2 ** (32-i)-2)
#7
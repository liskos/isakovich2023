import ipaddress
ip = ipaddress.ip_address('156.77.32.127')
for i in range(1, 32):
    net = ipaddress.ip_network(f'156.77.117.78/{i}', 0)
    if ip in net:
        print(net)
#17
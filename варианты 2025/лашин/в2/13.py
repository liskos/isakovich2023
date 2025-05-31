import ipaddress



ip2 = ipaddress.ip_address('234.212.8.43')

x = []
for i in range(10, 32):
    net = ipaddress.ip_network(f'234.212.9.32/{i}', 0)
    if ip2 in net:
        print(net)
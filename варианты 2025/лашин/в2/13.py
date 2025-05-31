import ipaddress


ip1 = ipaddress.ip_address('234.212.9.32')
ip2 = ipaddress.ip_address('234.212.8.43')

for i in range(10, 32):
    net1 = ipaddress.ip_network(f'{ip1}/{i}', 0)
    net2 = ipaddress.ip_network(f'{ip2}/{i}', 0)
    if ip1 in net2 and ip2 in net1:
        print(i)
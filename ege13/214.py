import ipaddress
ip1 = ipaddress.ip_address('193.45.192.104')
ip2 = ipaddress.ip_address('193.45.206.210')
for i in range(1, 32):
    net1 = ipaddress.ip_network(f'193.45.192.104/{i}', 0)
    net2 = ipaddress.ip_network(f'193.45.206.210/{i}', 0)
    if ip2 in net1 and ip1 in net2:
        if ip1.__format__('b').count('1') % 2 == 0 and ip2.__format__('b').count('1') % 2 == 0:
            print(ip1, ip2)
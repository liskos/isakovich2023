import ipaddress
ip1 = ipaddress.ip_address('193.45.192.104')
ip2 = ipaddress.ip_address('193.45.206.210')
for i in range(1, 32):
    net1 = ipaddress.ip_network(f'193.45.192.104/{i}', 0)
    net2 = ipaddress.ip_network(f'193.45.206.210/{i}', 0)
    if ip2 in net1 and ip1 in net2:
        print(net1.netmask, net2.netmask)
#240
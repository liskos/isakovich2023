import ipaddress
ip1 = ipaddress.ip_address('154.63.206.129')
ip2 = ipaddress.ip_address('154.63.100.75')
for i in range(1, 32):
    net1 = ipaddress.ip_network(f'154.63.206.129/{i}', 0)
    net2 = ipaddress.ip_network(f'154.63.100.75/{i}', 0)
    if ip2 not in net1 and ip1 not in net2:
        print(net1.netmask, net2.netmask)
#128
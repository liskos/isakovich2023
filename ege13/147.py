import ipaddress
ip1 = ipaddress.ip_address('191.131.175.201')
ip2 = ipaddress.ip_address('191.131.160.170')

for i in range(10, 32):
    net1 = ipaddress.ip_network(f'191.131.175.201/{i}', 0)
    net2 = ipaddress.ip_network(f'191.131.160.170/{i}', 0)
    if ip1 not in net2 and ip2 not in net1:
        if (ip1 != net1[-1]) and (ip2 != net2[0]):
            print(net1, net1.netmask)
#24
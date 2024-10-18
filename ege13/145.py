import ipaddress
ip1 = ipaddress.ip_address('198.75.95.31')
ip2 = ipaddress.ip_address('198.75.96.13')

for i in range(10, 32):
    net1 = ipaddress.ip_network(f'198.75.95.31/{i}', 0)
    net2 = ipaddress.ip_network(f'198.75.96.13/{i}', 0)
    if ip1 not in net2 and ip2 not in net1:
        if (ip1 != net1[-1]) and (ip2 != net2[-1]):
            print(net1, net1.netmask)
#24
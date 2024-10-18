import ipaddress
ip1 = ipaddress.ip_address('211.188.211.49')
ip2 = ipaddress.ip_address('211.188.200.115')
for i in range(1, 32):
    net1 = ipaddress.ip_network(f'211.188.211.49/{i}', 0)
    net2 = ipaddress.ip_network(f'211.188.200.115/{i}', 0)
    if ip2 not in net1 and ip1 not in net2:
        print(net1.netmask, net2.netmask)
#240
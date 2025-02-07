import ipaddress


for i in range(10, 30):
    ip1 = ipaddress.ip_address('3.120.77.205')
    ip2 = ipaddress.ip_address('3.120.77.131')
    net1 = ipaddress.ip_network(f'3.120.77.205/{i}', 0)
    net2 = ipaddress.ip_network(f'3.120.77.131/{i}', 0)
    if ip2 not in net1.hosts() and ip1 not in net2.hosts():
        print(net1, net2, net1[0], net1[-1], net2[0], net2[-1], net1.netmask)
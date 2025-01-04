import ipaddress

ip1 = ipaddress.ip_address('200.154.190.12')
ip2 = ipaddress.ip_address('200.154.184.0')
for i in range(32):
    net1 = ipaddress.ip_network(f'200.154.190.12/{i}', 0)
    net2 = ipaddress.ip_network(f'200.154.184.0/{i}', 0)
    if net1 == net2:
        print(net1, net2)
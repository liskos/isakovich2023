import ipaddress

ip1 = ipaddress.ip_address('192.168.82.70')
ip2 = ipaddress.ip_address('192.168.96.54')

for i in range(1, 32):
    net1 = ipaddress.ip_network(f'192.168.82.70/{i}', 0)
    net2 = ipaddress.ip_network(f'192.168.96.54/{i}', 0)
    if ip1 not in net2 and ip2 not in net1:
        print(net1, net2)
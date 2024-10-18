import ipaddress
ip1 = ipaddress.ip_address('145.207.153.178')
ip2 = ipaddress.ip_address('145.207.153.165')

for i in range(10, 32):
    net1 = ipaddress.ip_network(f'145.207.153.178/{i}', 0)
    net2 = ipaddress.ip_network(f'145.207.153.165/{i}', 0)
    if ip1 not in net2 and ip2 not in net1:
        if ip1 in net1.hosts() and ip2 in net2.hosts():
            print(net1, net1.netmask)
#24
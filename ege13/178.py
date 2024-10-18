import ipaddress

ip = ipaddress.ip_address('120.216.74.153')
for i in range(12, 32):
    net = ipaddress.ip_network(f'120.216.0.0/{i}', 0)
    if ip in list(net)[1:-1]:
        print(net, net.netmask)
print(2**(32-13))
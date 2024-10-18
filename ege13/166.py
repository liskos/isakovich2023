import ipaddress
k = 0
net = ipaddress.ip_network('139.75.100.0/255.255.252.0')
for ip in net:
    print(ip.__format__('b'), ip)

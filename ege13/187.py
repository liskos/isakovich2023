import ipaddress
c = []
net = ipaddress.ip_network('204.252.0.0/255.255.0.0')
for ip in net:
    c.append(ip.__format__('b').count('1'))
print(max(c))
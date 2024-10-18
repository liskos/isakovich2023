import ipaddress
c = []
net = ipaddress.ip_network('94.159.76.0/255.255.255.128')
for ip in net:
    c.append(ip.__format__('b').count('0'))
print(min(c))
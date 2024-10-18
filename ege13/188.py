import ipaddress
c = []
net = ipaddress.ip_network('135.221.128.0/255.255.128.0')
for ip in net:
    c.append(ip.__format__('b').count('1'))
print(min(c))
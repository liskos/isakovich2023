import ipaddress
c = []
net = ipaddress.ip_network('124.8.0.0/255.248.0.0')
for ip in net:
    c.append(ip.__format__('b').count('0'))
print(max(c))
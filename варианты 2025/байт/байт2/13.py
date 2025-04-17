import ipaddress
k = 0

net = ipaddress.ip_network('10.128.0.0/255.255.192.0')

for ip in net:
    if ip.__format__('b').count('1') % 4 == 0:
        k += 1
print(k)
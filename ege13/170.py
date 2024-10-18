import ipaddress
k = 0
net = ipaddress.ip_network('174.114.120.0/255.255.252.0')
for ip in net:
    if ip.__format__('b').count('1') % 2 == 0:
        k+=1
        print(ip.__format__('b'))
print(k)
import ipaddress
k = 0

net = ipaddress.ip_network('172.16.80.0/255.255.248.0')
for ip in net:
    if ip.__format__('b').count('1') % 2 > 0:
        k+=1
print(k)
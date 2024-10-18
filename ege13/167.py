import ipaddress
k = 0
net = ipaddress.ip_network('140.19.96.0/255.255.248.0')
for ip in net:
    if (ip.packed[0].__format__('b').count('1') == ip.packed[1].__format__('b').count('1') == ip.packed[2].__format__('b').count('1')
        == ip.packed[3].__format__('b').count('1')):
        k+=1
print(k)
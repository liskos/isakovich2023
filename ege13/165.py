import ipaddress
k = 0
net = ipaddress.ip_network(f'192.168.0.68/255.255.128.0', 0)
for ip in net:
    if int(ip.__format__('b'), 2) % 4 == 0:
        k+=1
print(k)

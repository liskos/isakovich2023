import ipaddress
k = 0
net = ipaddress.ip_network('184.178.54.144/255.255.255.240')
for ip in net:
    if '111' in ip.__format__('b'):
        print(ip.__format__('b'))
        k+=1
print(k)

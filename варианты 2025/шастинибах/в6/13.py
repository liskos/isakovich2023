import ipaddress

k = 0
net = ipaddress.ip_network('222.121.128.0/255.255.224.0')
for ip in net:
    if ip.__format__('b')[-2:] == '11' or ip.__format__('b')[-2:] == '00':
        k += 1
print(k)

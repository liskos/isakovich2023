import ipaddress

k = 0
net = ipaddress.ip_network('192.168.32.160/255.255.255.240')
for i in net:
    if i.__format__('b').count('0') > 21:
        print(i, i.__format__('b'))
        k+=1
print(k)
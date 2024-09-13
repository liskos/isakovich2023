import ipaddress

k = 0

net = ipaddress.ip_network('228.172.236.0/255.255.240.0', 0)
for i in net:
    if i.__format__('b').count('1') % 5 != 0:
        k += 1
print(k)

import ipaddress
k = 0
net = ipaddress.ip_network('139.75.100.0/255.255.252.0')
for ip in net:
    if ip.packed[-1] in [1,3,7,15,31,63,127,255]:
        k+=1
print(k)
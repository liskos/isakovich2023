import ipaddress


ip = ipaddress.ip_address('111.233.75.16')
k = 0
net = ipaddress.ip_network('111.233.75.16/111.233.75.0')
for ip in net:
    k += 1
print(k)
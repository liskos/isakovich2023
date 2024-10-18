import ipaddress
k = 0
net = ipaddress.ip_network('117.32.0.0/255.224.0.0')
for ip in list(net)[1:-1]:
    if len(set([ip.packed[0], ip.packed[1], ip.packed[2], ip.packed[3]])) == 3:
        k+=1
print(k)
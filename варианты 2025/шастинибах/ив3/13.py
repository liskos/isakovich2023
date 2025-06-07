import ipaddress


k = 0
net = ipaddress.ip_network('123.222.111.192/255.255.255.192', 0)
for ip in net:
    if (ip.__format__('b')[6:].count('0') + bin(222)[2:].count('0')) % 5 != 0:
        k += 1
print(k)
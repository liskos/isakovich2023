import ipaddress



net = ipaddress.ip_network('111.194.0.0/255.254.0.0', 0)
k = 0
for ip in net:
    if (ip.__format__('b').count('1') - ip.__format__('b').count('0')) % 2 == 0:
        k += 1
print(k)
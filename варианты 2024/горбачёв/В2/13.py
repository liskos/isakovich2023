import ipaddress


net = ipaddress.ip_network('82.230.106.168/255.255.255.240', 0)
k = 0
for ip in net:
    if (ip.packed[1].__format__("b").count("1")+ip.packed[2].__format__("b").count("1")) % 3 == 0:
        k += 1
print(k)
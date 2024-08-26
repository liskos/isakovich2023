import ipaddress

# net = ipaddress.ip_network("192.168.0.3/255.255.252.0", 0)
# print(list(net.hosts()))
# for i in net:
#     print(i.__format__("b"))


ip = ipaddress.ip_address("162.198.75.44")
ma = ipaddress.ip_address("255.255.240.0")
print(ip.__format__("b"))
print(ma.__format__("b"))
print(int("101100101100", 2))
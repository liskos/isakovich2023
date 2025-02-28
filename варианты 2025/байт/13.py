import ipaddress


ip1 = ipaddress.ip_address('192.168.100.0')
ip2 = ipaddress.ip_address('192.168.100.16')

net1 = ipaddress.ip_network('192.168.100.0/255.255.255.240')
net2 = ipaddress.ip_network('192.168.100.16/255.255.255.240')
net3 = ipaddress.ip_network('192.168.100.16/255.255.255.224', 0)
print(ip1.__format__("b"))
print(net1.netmask.__format__("b"))
print(ip2.__format__("b"))
print(net2.netmask.__format__("b"))
print(net3.netmask.__format__("b"))
import ipaddress


ip1 = ipaddress.ip_address('192.168.100.0')
ip2 = ipaddress.ip_address('192.168.100.16')

net1 = ipaddress.ip_network('192.168.100.0/255.255.255.240')
net2 = ipaddress.ip_network('192.168.100.16/255.255.255.240')


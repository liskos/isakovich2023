import ipaddress


m = ipaddress.ip_network('192.168.0.0/255.255.254.0')
print(len(list(m.hosts())))
import ipaddress


ip = ipaddress.ip_address("172.16.168.0")
ma = ipaddress.ip_address("255.255.248.0")
print(ip.__format__("b"))
print(ma.__format__("b"))

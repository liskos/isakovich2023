import ipaddress

ip = ipaddress.ip_address("255.255.255.248")
ma = ipaddress.ip_address("156.128.0.227")
print(ip.__format__("b"))
print(ma.__format__("b"))
print(int("011", 2))
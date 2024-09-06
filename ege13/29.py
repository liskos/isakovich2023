import ipaddress

ip = ipaddress.ip_address("162.198.0.157")
ma = ipaddress.ip_address("255.255.255.224")
print(ip.__format__("b"))
print(ma.__format__("b"))
print(int("11101", 2))
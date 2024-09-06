import ipaddress

ip = ipaddress.ip_address("206.158.124.67")
ma = ipaddress.ip_address("255.255.224.0")
print(ip.__format__("b"))
print(ma.__format__("b"))
print(int("1110001000011", 2))
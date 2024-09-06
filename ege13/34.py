import ipaddress

ip = ipaddress.ip_address("156.132.15.138")
ma = ipaddress.ip_address("255.255.252.0")
print(ip.__format__("b"))
print(ma.__format__("b"))
print(int("1110001010", 2))
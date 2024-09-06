import ipaddress

ip = ipaddress.ip_address("132.126.150.18")
ma = ipaddress.ip_address("255.255.240.0")
print(ip.__format__("b"))
print(ma.__format__("b"))
print(int("011000010010", 2))
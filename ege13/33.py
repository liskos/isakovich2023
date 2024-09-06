import ipaddress

ip = ipaddress.ip_address("122.191.12.189")
ma = ipaddress.ip_address("255.255.255.128")
print(ip.__format__("b"))
print(ma.__format__("b"))
print(int("0111101", 2))
import ipaddress

ip = ipaddress.ip_address("112.154.133.208")
ma = ipaddress.ip_address("255.255.248.0")
print(ip.__format__("b"))
print(ma.__format__("b"))
print(int("10111010000", 2))
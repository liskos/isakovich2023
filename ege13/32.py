import ipaddress

ip = ipaddress.ip_address("255.255.255.192")
ma = ipaddress.ip_address("10.18.134.220")
print(ip.__format__("b"))
print(ma.__format__("b"))
print(int("011100", 2))
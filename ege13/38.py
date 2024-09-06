import ipaddress

ip = ipaddress.ip_address("126.185.90.162")
ma = ipaddress.ip_address("255.255.252.0")
print(ip.__format__("b"))
print(ma.__format__("b"))
print(int("1010100010", 2))
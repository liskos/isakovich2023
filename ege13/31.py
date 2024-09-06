import ipaddress

ip = ipaddress.ip_address("255.255.255.240")
ma = ipaddress.ip_address("192.168.156.235")
print(ip.__format__("b"))
print(ma.__format__("b"))
print(int("1011", 2))
import ipaddress


m = ipaddress.ip_address('255.255.255.128')
b = m.__format__('b')
print(m.__format__('b'))
print(2 ** b.count('0') - 2)
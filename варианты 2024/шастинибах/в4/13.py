import ipaddress


ip = ipaddress.ip_address('222.190.122.24')
for i in range(1, 32):
    net = ipaddress.ip_network(f'222.190.120.0/{i}', 0)


import ipaddress


ip = ipaddress.ip_address('222.190.122.24')
for i in range(15, 32):
    net = ipaddress.ip_network(f'222.190.122.24/{i}', 0)
    print(net)
print(2**11-3)


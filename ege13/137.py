import ipaddress
ip = ipaddress.ip_address('145.207.153.178')
for i in range(1, 32):
    net = ipaddress.ip_network(f'145.207.153.165/{i}', 0)
    if ip in net:
        print(net)
#27
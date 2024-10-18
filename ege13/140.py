import ipaddress
ip = ipaddress.ip_address('112.166.78.114')
for i in range(1, 32):
    net = ipaddress.ip_network(f'112.166.78.117/{i}', 0)
    if ip in net:
        print(net)
#29
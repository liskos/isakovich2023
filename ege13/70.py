import ipaddress


ip = ipaddress.ip_address('115.127.30.120')
for i in range(1, 32):
    net = ipaddress.ip_network(f'115.127.151.120/{i}',0)
    if ip in net:
        print(net, net.netmask)
#0

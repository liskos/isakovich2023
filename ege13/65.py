import ipaddress


ip = ipaddress.ip_address('220.128.114.142')
for i in range(1, 32):
    net = ipaddress.ip_network(f'220.128.64.0/{i}',0)
    if ip in net:
        print(net, net.netmask)
#192

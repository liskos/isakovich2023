import ipaddress


ip = ipaddress.ip_address('220.127.169.27')
for i in range(1, 32):
    net = ipaddress.ip_network(f'220.127.160.0/{i}', 0)
    if ip in net:
        print(net, net.netmask)
#19
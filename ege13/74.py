import ipaddress


ip = ipaddress.ip_address('121.171.15.70')
for i in range(1, 32):
    net = ipaddress.ip_network(f'121.171.3.68/{i}',0)
    if ip in net:
        print(net, net.netmask)
#240

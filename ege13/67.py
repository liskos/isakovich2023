import ipaddress


ip = ipaddress.ip_address('117.191.88.37')
for i in range(1, 32):
    net = ipaddress.ip_network(f'117.191.80.0/{i}',0)
    if ip in net:
        print(net, net.netmask)
#240

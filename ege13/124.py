import ipaddress


ip = ipaddress.ip_address('124.145.64.28')
for i in range(1, 32):
    net = ipaddress.ip_network(f'124.145.64.0/{i}', 0)
    if ip in net:
        print(net, net.netmask)
#10
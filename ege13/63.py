import ipaddress


ip = ipaddress.ip_address('124.32.48.131')
for i in range(1, 32):
    net = ipaddress.ip_network(f'124.32.32.0/{i}',0)
    if ip in net:
        print(net, net.netmask)
#224
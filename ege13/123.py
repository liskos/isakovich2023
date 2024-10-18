import ipaddress


ip = ipaddress.ip_address('116.123.64.53')
for i in range(1, 32):
    net = ipaddress.ip_network(f'116.123.64.0/{i}', 0)
    if ip in net:
        print(net, net.netmask)
#9
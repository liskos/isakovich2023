import ipaddress


for i in range(24, 32):
    net = ipaddress.ip_network(f'172.16.168.0/{i}', 0)
    a = []
    for ip in net:
        if ip.__format__('b').count('0') % 7 == 0:
            a.append(ip)
    print(net, len(a), net.netmask)
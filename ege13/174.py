import ipaddress

ip = ipaddress.ip_address('193.22.209.132')
for i in range(1, 32):
    net = ipaddress.ip_network(f'193.22.209.128/{i}', 0)
    print(net, net.netmask)
#1
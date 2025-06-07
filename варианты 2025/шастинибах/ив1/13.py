import ipaddress


for i in range(32):
    net = ipaddress.ip_network(f'192.214.116.184/{i}', 0)
    print(net, net[0].__format__('b').count('1'))
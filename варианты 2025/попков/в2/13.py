import ipaddress


for i in range(16, 25):
    net = ipaddress.ip_network(f'219.127.14.47/{i}', 0)
    for ip in net:
        if not ip.packed[0].__format__('b').count('1') + ip.packed[1].__format__('b').count('1') >= ip.packed[2].__format__('b').count('1') + ip.packed[3].__format__('b').count('1'):
            break
    else:
        print(net, net.netmask)

import ipaddress
k = 0
ip = ipaddress.ip_address('193.22.209.132')
for i in range(15, 32):
    net = ipaddress.ip_network(f'193.22.209.128/{i}', 0)
    if ip in list(net)[1:-1]:
        print(net)

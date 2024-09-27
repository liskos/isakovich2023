import ipaddress


ip = ipaddress.ip_address('111.81.208.27')
for i in range(1, 32):
    net = ipaddress.ip_network(f'111.81.192.0/{i}',0)
    if ip in net and str(net).split("/")[0]=="111.81.192.0":
        print(net, net.netmask.packed[2])
#224

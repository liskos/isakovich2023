import ipaddress


for i in range(0, 256):
    ip = ipaddress.ip_address(f'192.214.{i}.184')
    net = ipaddress.ip_network(f'192.214.{i}.184/255.255.255.224', 0)
    if ip not in [net[0], net[-1]]:
        if all(bin(int(ip))[2:].zfill(32).count('1') > 15 for ip in net):
            print(i)
            break
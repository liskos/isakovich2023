import ipaddress


net = ipaddress.ip_network('98.71.254.171/255.248.0.0', 0)

for ip in net:
    if ip.__format__('b').count('1') % 5 == 0:
        print(ip)
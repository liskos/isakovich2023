import ipaddress


net = ipaddress.ip_network('82.230.106.168/255.255.255.240')
for ip in net:
    if 
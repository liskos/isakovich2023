import ipaddress

ip = ipaddress.ip_address('123.222.111.192')
net = ipaddress.ip_network('123.222.111.192/255.255.255.248')
for ip in net:
    print(ip.__format__('b'))
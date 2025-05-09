import ipaddress


net = ipaddress.ip_network('98.71.254.171/255.248.0.0', 0)
s = ""
for ip in net.hosts():
    if ip.__format__('b').count('1') % 5 == 0:
        s = str(ip).replace(".", "")
print(s)
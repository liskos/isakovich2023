import re

a = open('24.txt').read()
num = r'(([1-6][0-6]*)|[0])'
proizv = rf'(({num}[*])*{num})'
summa = rf'{proizv}'
summa2 = rf'(({num}[+])*{num})'
d = [x.group() for x in re.finditer(summa, a)]
ma = max(d, key=len)
print(len(ma), ma)
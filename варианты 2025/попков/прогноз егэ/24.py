import re

a = open('24.txt').readline()
num = r'(([1-9][0-9]*[24568])|([024568]))'
proizv = rf'(({num}[*])*0([*]{num})*)'
summa = rf'({proizv}[+])*{proizv}'
r = [x.group() for x in re.finditer(summa, a)]
m = max(r, key=len)
print(len(m), m)

a = open('24data/24-299.txt').read()

import re
number = r'(([1-9][0-9]*)|0)'
vir = rf'(({number}[*])*[0]([*]{number})*)'
pattern = rf'{vir}([+]{vir})*'

d = [x.group() for x in re.finditer(pattern, a)]
m = max(d, key=len)
print(len(m))
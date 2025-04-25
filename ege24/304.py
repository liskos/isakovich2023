a = open('24data/24-304.txt').read()

import re
number = r'(([1-9][0-9]*)|0)'

pattern = rf'[A]+{number}([+*]{number})+'

d = [x.group() for x in re.finditer(pattern, a)]
print(d)
m = max(d, key=len)
print(len(m), m)

a = open('24data/24-264.txt').read()

import re

pattern = r'[0-9A-F]+'

d = max([x.group() for x in re.finditer(pattern, a)], key=len)
print(len(d), d)
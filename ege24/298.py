a = open('24data/24-298.txt').read()

import re


pattern = r'[789]+[-*]?[7890]+'

d = max([x.group() for x in re.finditer(pattern, a)], key=len)
print(len(d))
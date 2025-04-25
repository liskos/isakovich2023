a = open('24data/24-221.txt').read()

import re

pattern = r'(0)+(1)+'
d = max([x.group() for x in re.finditer(pattern, a)], key=len)
print(len(d))
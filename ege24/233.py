a = open('24data/24-233.txt').read()

import re

pattern = r'[A-Z]{1}[1-9]+[0-9]+[A-Z]{1}'


d = max([x.group() for x in re.finditer(pattern, a)], key=len)
print(d)
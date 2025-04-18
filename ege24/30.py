a = open('24data/k7b-4.txt').read()

import re

pattern = r'(EBCF)+(EBC|EB|E)?'
r = max([x.group() for x in re.finditer(pattern, a)], key=len)
print(len(r), r)
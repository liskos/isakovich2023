a = open('24data/k7b-1.txt').read()

import re

pattern = r'(EAB)+(EA|E)?'
r = max([x.group() for x in re.finditer(pattern, a)], key=len)
print(len(r), r)
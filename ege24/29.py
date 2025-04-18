a = open('24data/k7b-3.txt').read()

import re

pattern = r'(BAFE)+(BAF|BA|B)?'
r = max([x.group() for x in re.finditer(pattern, a)], key=len)
print(len(r), r)
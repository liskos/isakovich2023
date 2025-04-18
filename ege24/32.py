a = open('24data/k7b-6.txt').read()

import re

pattern = r'(DAF)+(DA|D)?'
r = max([x.group() for x in re.finditer(pattern, a)])
print(len(r), r)
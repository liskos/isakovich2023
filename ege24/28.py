a = open('24data/k7b-2.txt').read()

import re

pattern = r'(DBAC)+(DBA|DB|D)?'
r = max([x.group() for x in re.finditer(pattern, a)], key=len)
print(len(r), r)
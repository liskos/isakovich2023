a = open('24data/k7b-5.txt').read()

import re

pattern = r'(?:CA)+'
r = max([x.group() for x in re.finditer(pattern, a)])
print(len(r), r)
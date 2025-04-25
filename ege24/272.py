a = open('24data/24-264.txt').read()

import re


pattern = r'([A-Z0-9]+)(^\1+)'

d = [x.group() for x in re.finditer(pattern, a)]
print(d)
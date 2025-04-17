a = open('24data/k7c-1.txt').read()

import re


pattern = r'([BDE]{1})([^\1]){1}([^\2]){1}'
a = re.sub(r'[F]', ' ', a)
r = [x.group() for x in re.finditer(pattern, a)]
print(r)
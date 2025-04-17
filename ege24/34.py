a = open('24data/k7c-1.txt').read()

import re


pattern = r'([ACE]{1})([^\1]){1}([^\2]){1}'
a = re.sub(r'[E]', ' ', a)
r = [x.group() for x in re.finditer(pattern, a)]
print(r)
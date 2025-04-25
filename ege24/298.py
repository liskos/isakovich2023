a = open('24data/24-298.txt').read()

import re

number = r'([789][0789]*)'
pattern = rf'{number}([*-]{number})+'

d = max([x.group() for x in re.finditer(pattern, a)], key=len)
print(len(d))
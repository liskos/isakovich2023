import re

a = open('24_21509.txt').read()

number = r'(([789][0789]*)|0)'
pattern = rf'{number}([-*]{number})+'
c = max([x.group() for x in re.finditer(pattern, a)], key=len)
print(len(c), c)

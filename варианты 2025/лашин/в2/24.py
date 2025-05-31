import re
a = open('24.txt').read()

numb = r'(([1-9][0-9]+)|[0-9])'
pattern = rf'({numb}[+])*{numb}'

r = [x.group() for x in re.finditer(pattern, a)]
m = max(r, key=len)
print(len(m[12:]), m[12:])
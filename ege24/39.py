import re

a = open('24data/k7-m1.txt').read()

pattern = r'C+'

m = [x.group() for x in re.finditer(pattern, a)]
print(len(min(m, key=len)), len(m), len(a))
s = open('24data/k7-2.txt').read()
print(s)
t = 'C'
while t in s:
    t += 'C'
print(t)
import re
pattern = r'[C]+'
r = [x.group() for x in re.finditer(pattern, s)]
print(r)
r2 = max([len(x) for x in r])
print(r2)
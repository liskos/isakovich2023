import re
s = open('24.txt').read()

pattern = r'([1-9AB][0-9AB]*[02468A])|([02468A])'
r = [x.group() for x in re.finditer(pattern, s)]
m = max(r, key=len)
print(m, len(m))
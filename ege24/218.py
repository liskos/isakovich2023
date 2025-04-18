import re
a = open('24data/24-215.txt').read()


pattern = r'([1-3][1-3][A-C])+'
m = max([x.group() for x in re.finditer(pattern, a)], key=len)
print(len(m) // 3, m)
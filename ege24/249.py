a = open('24data/24-249.txt').read()
import re

pattern = r'([0-9A-F]+)'

d = [x.group() for x in re.finditer(pattern, a)]
print(d)
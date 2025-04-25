a = open('24data/24-241.txt').read()
import re


pattern = r'([BCDF]{1}[BCDF]{1}[AEO]{1})+'


d = max([x.group() for x in re.finditer(pattern, a)], key=len)

print(len(d))



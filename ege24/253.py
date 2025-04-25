a = open('24data/24-253.txt').read()
import re


pattern = r'([CDF]{1}[ACDFO]{1}[AO]{1})+'

d = max([x.group() for x in re.finditer(pattern, a)], key=len)

print(len(d)//3)

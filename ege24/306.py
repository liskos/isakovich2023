a = open('24data/24-306.txt').read()
import re

number = r'([1-9][0-9]*|0)'
pattern = rf'AFD{number}([+*]{number})+'

d = [x.group() for x in re.finditer(pattern, a)]
m = max(d, key=len)
print(len(m), m)
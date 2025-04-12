s = open('24data/k7a-4.txt').read()
# s = s.replace('D', ' ')
# print(max(map(len, s.split())))

# t = ''
# m = 0
# for i in s:
#     t += i
#     while 'D' in t:
#         t = t[1:]
#     m = max(m, len(t))
# print(m)
import re

pattern = r'[^D]+'
r = [len(x.group()) for x in re.finditer(pattern, s)]
print(max(r))
import sys

sys.stdin = open('24.txt')
s = input()
x = s[0]
m = 1
t = 1
for i in s[1:]:
    if (x in 'AEIOUY') == (i in 'AEIOUY'):
        t += 1
    else:
        t = 1
    m = max(t, m)
    x = i
print(m)
import sys
sys.stdin = open('24.txt')

a = input()
a = a.replace('**', '* *').replace('**', '* *')
a = a.replace('--', '- -').replace('--', '- -')
a = a.replace('*-', '* -').replace('*-', '* -')
a = a.replace('-*', '- *').replace('-*', '- *')

b = a.split()
c = []
for s in b:
    if s[0] == '*' and s[-1] == '*':
        c.append(s[1:-1])

for s in b:
    if s[-1] == '-':
        c.append(s[:-1])
d = []
g = []
for s in b:
        while s[:2] == '00':
            s = s[1:]
        if len(s) > 1 and s[0] == "0" and s[1].isdigit():
            s = s[1:]
        d.append(len(s))
        g.append(s)



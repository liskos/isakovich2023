import sys
sys.stdin = open('24.txt')
a = input()
a = a.replace('**', '* *').replace('**', '* *')
a = a.replace('--', '- -').replace('--', '- -')
a = a.replace('*-', '* -').replace('*-', '* -')
a = a.replace('-*', '- *').replace('-*', '- *')
for i in range(10):
    a = a.replace("*0"+str(i), "*0 "+str(i))
    a = a.replace("-0"+str(i), "-0 "+str(i))

a = a.split()
b = []
c = []
for s in a:
    if s[0] == '*':
        b.append(s[1:])
    elif s[0] == '-':
        b.append(s[1:])
    else:
        b.append(s)
for s in b:
    if s:
        if s[-1] == '*':
            c.append(s[:-1])
        elif s[-1] == '-':
            c.append(s[:-1])
        else:
            c.append(s)
d = []
for s in c:
        while s[:2] == '00':
            s = s[1:]
        if len(s) > 1 and s[0] == "0" and s[1].isdigit():
            s = s[1:]
        d.append(s)
m = 0
for s in d:
    m = max(m, len(s))
print(m)
for s in d:
    if len(s) == 154:
        print(s)
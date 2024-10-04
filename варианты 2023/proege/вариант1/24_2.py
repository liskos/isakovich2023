import sys
sys.stdin = open('24.txt')
s = input()
m = 0
a = ""
for i in s:
    if i in "0123456789ABCDEF":
        a += i
    else:
        a += " "
for i in a.split():
    t = i
    while t[0] == '0':
        t = t[1:]
    m = max(m, len(t))

print(m)
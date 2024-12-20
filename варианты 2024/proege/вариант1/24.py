import sys
sys.stdin = open('24.txt')
a = input()
m = 0
for i in 'GHIJKLMNOPQRSTUVWXYZ':
    a = a.replace(i, ' ')
for s in a.split():
    t = s
    while t[0] == '0':
        t = t[1:]
    m = max(m, len(t))

print(m)
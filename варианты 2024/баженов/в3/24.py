import sys
sys.stdin = open('24.txt')
s = input()
m = 0
t = ''
s = s.replace('B', 'A').replace('C', 'A').replace('D', 'A')
for i in s:
    t += i
    while 'AA' in t:
        t = t[1:]
    m = max(m, len(t))
print(m)
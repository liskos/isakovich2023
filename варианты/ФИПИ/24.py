import sys

sys.stdin = open('24.txt')
s = input()
s = s.replace('R', 'Q').replace('W', 'Q').replace('4', '1').replace('2', '1')
t = ""
m = 0
for i in s:
    t = t + i
    while ("11" in t) or ("QQ" in t):
        t = t[1:]
    m = max(m, len(t))
print(m)

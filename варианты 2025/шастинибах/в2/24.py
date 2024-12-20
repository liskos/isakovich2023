import sys
sys.stdin = open('24.txt')
s = input()
c = []
s = s.replace('X', ' ').split()
d = max([x.count('Y') for x in s])
v = [x for x in s if x.count('Y') == 75]
print(v, len(v[0]), len(v[1]))


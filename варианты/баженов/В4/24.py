import sys

sys.stdin = open('24.txt')
a = input()
t = 'ABC'
while t in a:
    t += 'ABC'
t = t[1:] + 'A'
print(len(t))
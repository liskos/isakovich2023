import sys
sys.stdin = open('26.txt')

t = ['0'] * 44640
n = int(input())
for i in range(n):
    t1, t2 = map(int, input().split())
    for x in range(t1, t2):
        t[x] = '1'
a = ''.join(t)
a = max(map(len, a.split('0')))
print(t.count('1'), a)
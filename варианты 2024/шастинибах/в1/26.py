import sys
sys.stdin = open('26.txt')
n, v = map(int, input().split())
a = sorted([int(input()) for _ in range(n)], reverse=True)
k = 0
p = 0
v = 1000 * v
c = 0
for i in range(len(a)):
    if a[i] <= v - k and 7000 <= a[i] <= 12000:
        k += a[i]
        p = a[i]
        c += 1
print(c, p)
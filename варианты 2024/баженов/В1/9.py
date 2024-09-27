import sys
sys.stdin = open('9.txt')

k = 0
for i in range(5000):
    a = sorted(map(int, input().split()))
    if (a[2]**2 == a[0]**2 + a[1]**2) or (a[0] % 10 > 7 and a[1] % 10 > 7 and a[2] % 10 > 7):
        k += 1
print(k)
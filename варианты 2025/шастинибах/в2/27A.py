import sys, func




sys.stdin = open('27A.txt')
kl_a = []
kl_b = []

for i in range(96):
    x, y = map(float, input().split())
    if x > 1 and y > 3:
        kl_a.append([x, y])
    else:
        kl_b.append([x, y])
print(func.func(kl_a,kl_b))
#1731 6256
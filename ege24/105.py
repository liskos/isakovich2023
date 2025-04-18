a = open('24data/24-2.txt').read()

t = ''
m = 0
i_best = 0
for i in range(len(a)):
    if not t:
        t = a[i]
    elif t[-1] < a[i]:
        t += a[i]
        if len(t) > m:
            m = len(t)
            i_best = i
    else:
        t = a[i]
print(i_best - m + 2)

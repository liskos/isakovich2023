s = open("24.txt").read()

t = ""
t_best = ""
m = 10**10
k = 0
for i in s:
    t += i
    if t[-3:] == "RSQ":
        k += 1
    while k > 130:
        if t[:3] == "RSQ":
            k -= 1
        t = t[1:]
    while k==130 and t[:3] != "RSQ":
        t = t[1:]
    if k == 130 and t[-1] != "Q":
        if len(t) < m:
            m = len(t)
            t_best = t
print(m, t_best)

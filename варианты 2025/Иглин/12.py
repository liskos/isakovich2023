
def f(s):
    while '222' in s or '555' in s:
        if '555' in s:
            s = s.replace('555', '2', 1)
        else:
            s = s.replace('222', '5', 1)
    return s

c=[]
for i in range(1, 1000):
    c.append(sum(map(int, (f('2' + i * '5')))))
print(max(c))
def f(n):
    while ('14' in n) or ('7444' in n) or ('4444' in n) or ('717' in n):
        if '14' in n:
            n = n.replace('14','44',1)
        if '7444' in n:
            n = n.replace('7444', '1', 1)
        if '4444' in n:
            n = n.replace('4444', '77', 1)
        if '717' in n:
            n = n.replace('717', '7', 1)
    return n

a = []
for i in range(4, 10000):
    a.append(len(f('1' + i * '4')))
    print(max(a))

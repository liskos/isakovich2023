def f(n):
    b = bin(n)[2:]
    if b.count('0') == b.count('1'):
        b = b + b[-1]
    else:
        if b.count('0') > b.count('1'):
            b = b + '1'
        else:
            b = b + '0'
    if b.count('0') == b.count('1'):
        b = b + b[-1]
    else:
        if b.count('0') > b.count('1'):
            b = b + '1'
        else:
            b = b + '0'
    if b.count('0') == b.count('1'):
        b = b + b[-1]
    else:
        if b.count('0') > b.count('1'):
            b = b + '1'
        else:
            b = b + '0'
    return int(b, 2)




a = []
for i in range(2, 500):
    if f(i) % 4 == 0 and f(i) % 8 != 0:
        a.append(i)
print(max(a))


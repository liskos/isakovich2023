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


for i in range(80, 1000):
    if f(i) % 4 == 0:
        print(i)
        break
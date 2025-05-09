def dig(a, b):
    return str(a)[0]== str(b)[0]


for a in range(1, 100):
    if all(not(not(dig(x, 28)) and (dig(x, 47))) or (x > a - 20) for x in range(1, 100)):
        print(a)
def dig(a, b):
    return a % 10 == b % 10


for a in range(100):
    if all(not(dig(x, 28)) and not(dig(x, 47)) or (x > a - 20) for x in range(100)):
        print(a)
def f(n):
    b = bin(n)[2:]
    if b % 2 == 1:
        b = b.replace('1', '2').replace('0','1').replace('2','0')
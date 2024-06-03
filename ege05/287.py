def f(n):
    b = bin(n)[2:]
    if n % 2 == 0:
        b = '1' + b + '11'
    else:
        b = '11' + b + '0'
    return int(b, 2)



print(f(13))
a = []
for i in range(1, 10000):
    if 500 <= f(i) <= 1000:
        a.append(i)
print(min(a))
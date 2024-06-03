def f(n):
    b = bin(n)[2:]
    if n % 2 == 0:
        b = '1' + b + '10'
    else:
        b = '11' + b + '0'
    return int(b, 2)



print(f(13))
a = set()
for i in range(1, 10000):
    if 800 <= f(i) <= 1500:
        a.add(f(i))
print(len(a))
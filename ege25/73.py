def f(n):
    a = set()
    for i in range(2, int(n ** 0.5)+1):
        if n % i == 0:
            a.add(i)
            a.add(n//i)
    a.add(1)
    return a


k = 0
for i in range(2, 20001):
    if sum(f(i)) > i:
        k+=1
print(k)


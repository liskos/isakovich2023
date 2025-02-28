def f(n):
    a = set()
    for i in range(1, int(n ** 0.5)+1):
        if n % i == 0:
            a.add(i)
            a.add(n//i)
    return a


k = 0
for i in range(2, 10001):
    if sum(f(i)) > i:
        k+=1
        print(len(f(i)), *sorted(f(i), reverse=True)[:2])
print(k)


def f(n):
    a = set()
    for i in range(2, int(n ** 0.5)+1):
        if n % i == 0 and i != n:
            a.add(i)
            a.add(n//i)
    return a

k = 0

for i in range(3661, 33625):
    if len(f(i)) == 1:
        k+=1
        print(len(f(i)), *sorted(f(i), reverse=True)[:2])
print(k)


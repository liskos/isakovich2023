def f(n):
    a = set()
    for i in range(2, int(n ** 0.5)+1):
        if n % i == 0:
            a.add(i)
            a.add(n//i)
    a.add(1)
    return a



for i in range(2, 10001):
    if sum(f(i)) == i:
        print(i, len(f(i)))


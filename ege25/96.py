def f(n):
    a = set()
    for i in range(2, int(n ** 0.5)+1):
        if n % i == 0:
            a.add(i)
            a.add(n//i)
    return a



for i in range(81234, 134689):
    if len(f(i)) == 3:
        print(f(i), *sorted(f(i), reverse=True)[:2])



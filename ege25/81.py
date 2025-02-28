def f(n):
    a = set()
    for i in range(1, int(n ** 0.5)+1):
        if n % i == 0:
            a.add(i)
            a.add(n//i)
    return a



for i in range(2, 263001):
    if sum(f(sum(f(i)))) == i * 2:
        print(len(f(i)), *sorted(f(i), reverse=True)[:2])



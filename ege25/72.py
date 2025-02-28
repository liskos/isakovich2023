def f(n):
    a = set()
    for i in range(1, int(n ** 0.5)+1):
        if n % i == 0:
            a.add(i)
            a.add(n//i)
    return a




for i in range(2, 20001):
    if len(f(i)) == 80:
        print(len(f(i)), *sorted(f(i), reverse=True)[:2])



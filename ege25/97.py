def f(n):
    a = set()
    for i in range(2, int(n ** 0.5)+1):
        if n % i == 0:
            a.add(i)
            a.add(n//i)
    return a



for i in range(135790, 163228+1):
    if sum(f(i)) > 460000:
        print(len(f(i)), sum(f(i)))



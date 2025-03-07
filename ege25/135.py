def f(n):
    a = set()
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            a.add(i)
            a.add(n//i)
    b = [x for x in a if x % 2 > 0]
    return b


for i in range(321654, 654322):
    if len(f(i)) > 70:
        print(i, max(f(i)))
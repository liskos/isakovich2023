def div(x):
    s = set()
    for i in range(1, int(x**0.5) + 1):
        if x % i == 0:
            diff = abs(x//i - i)
            if diff <= 120:
                s.add(diff)
    return sorted(s)

for i in range(2000000, 3000001):
    d = div(i)
    if len(d) >= 3 and max(d) <= 120:
        print(i, max(d))
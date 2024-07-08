a = []
for x in '0123456789abcdefg':
    n = int('9a51', 17) + (int(x, 17) * 17 ** 1) + int('4gb2', 17) + (int(x, 17) * 17 ** 0) + (int(x , 17) * 17 ** 3) + int('28d', 17) + (int(x, 17) * 17 ** 1)
    if n % 11 == 0:
        a.append(n // 11)
print(max(a))
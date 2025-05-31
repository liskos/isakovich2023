
for i in range(6437, 10**10, 6437):
    s = str(i)
    if s[0] == '1' and s[2] == '3' and s[-3:] == '954' and '5' in s[3:-3]:
        print(i, i // 6437)
a = []
for x in range(150):
    s = int('51029', 150) + (x * 150 ** 2) + int('0023', 150) + (x * 150 ** 3)
    if s % 149 == 0:
        a.append(x)
print(max(a))
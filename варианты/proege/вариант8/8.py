import itertools

a = []
for i in itertools.product('0234567', repeat=5):
    s = "".join(i)
    s = s.replace("2", "0").replace("4", "0").replace("6", "0")
    s = s.replace("5", "3").replace("7", "3")
    if i[0] != '0' and len(set(i)) == 5 and ("00" not in s) and ("33" not in s):
        a.append(i)
print(len(a))
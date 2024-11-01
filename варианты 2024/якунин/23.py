a = {155}
for _ in range(15):
    b = set()
    for x in a:
        b.add(x+5)
        b.add(x*2)
    a = b.copy()
print(len(a))
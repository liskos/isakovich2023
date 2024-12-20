k=0
for a in range(1, 50000):
    if all((x % a == 0) or (x % 120 == 0) or (x % 180 != 0) for x in range(1, 50000)):
        k+=1
print(k)
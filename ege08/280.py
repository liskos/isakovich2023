import itertools
k=0
for i in itertools.product('qwertyuiopasdfghjklzxcvbnm', repeat=5):
    if i.count('e') + i.count('y') + i.count('u') + i.count('i') + i.count('o') + i.count('a') > 0:
        k+=1
print(k)
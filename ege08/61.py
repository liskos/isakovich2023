import itertools


k = 0
for s in itertools.product('АБВГДЭЮЯ', repeat=5):
    if s[0] in 'ЭЮЯ' and s[-1] in 'ЭЮЯ' and set(s[1:-1]) <= {'А', 'Б', 'В', 'Г', 'Д'}:
        k+=1
print(k)



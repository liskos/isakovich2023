import itertools

k = 0

for i in itertools.permutations('ПРИКАЗ', r=4):
    ss = ''.join(i)
    if ss.count('И') + ss.count('А') <= 1:
        k+=1



print(k)

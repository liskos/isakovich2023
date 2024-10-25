import itertools

k = 0

for i in itertools.permutations('МАГИСТР', r=5):
    ss = ''.join(i)
    if ss.count('А') + ss.count('И') <= 1:
        k+=1



print(k)

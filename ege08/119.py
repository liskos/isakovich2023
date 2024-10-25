import itertools

k = 0

for i in itertools.product('МАГИСТР', repeat=5):
    ss = ''.join(i)
    if (ss.count('М') <= 1 and ss.count('А') <= 1 and
        ss.count('Г') <= 1 and ss.count('И') <= 1 and
        ss.count('С') <= 1 and ss.count('Т') <= 1 and
        ss.count('Р') <= 1):
        k+=1



print(k)

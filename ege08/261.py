import itertools

k=0
for s, i in enumerate(itertools.product('АЕЖЙМУ', repeat=5), 1):
    ss = ''.join(i)
    if 'АА' not in ss and 'ЕЕ' not in ss and 'ЖЖ' not in ss and 'ЙЙ' not in ss and 'ММ' not in ss and 'УУ' not in ss and s % 2 == 0:
        k+=1
print(k)
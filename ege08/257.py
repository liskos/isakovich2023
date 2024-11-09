import itertools

k=0
for s, i in enumerate(itertools.product('АЕПСТУХ', repeat=4), 1):
    ss = ''.join(i)
    if 'АА' not in ss and 'СС' not in ss and 'ТТ' not in ss and 'ЕЕ' not in ss and 'ПП' not in ss and 'УУ' not in ss and 'ХХ' not in ss and s > 1000:
        k+=1
print(k)
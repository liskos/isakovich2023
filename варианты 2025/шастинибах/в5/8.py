import itertools
c=[]
k = 0
for s in itertools.product('АВИЙКПС', repeat=6):
    ss = ''.join(s)
    if 'АА' in ss or 'ИИ' in ss or 'АИ' in ss or 'ИА' in ss:
        k += 1
        if 'КАКААА' in ss:
            print(k, ss)


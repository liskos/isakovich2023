import itertools


for s, i in enumerate(itertools.product('ГЕКЭ023', repeat=4), 1):
    ss = ''.join(i)
    if ss[0] in '023' and 'КК' not in ss and 'ЕЕ' not in ss and 'ГГ' not in ss and 'ЭЭ' not in ss and '22' not in ss and '00' not in ss and '22' not in ss and '33' not in ss:
        print(s, ss)
        break

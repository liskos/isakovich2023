import itertools

k = 0
for s in itertools.product('ДИОНИСИЙ', repeat=6):
    i = ''.join(s)
    if (('Д' in i and 'Н' not in i) or ('Д' not in i and 'Н' in i)) and 'ДД' not in i and 'ИИ' not in i and 'ОО' not in i and 'НН' not in i and 'СС' not in i and 'ЙЙ' not in i:
        print(i)
        k += 1
print(k)
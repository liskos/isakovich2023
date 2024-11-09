import itertools

k=set()
for i in itertools.product('СОЛНЦЕ', repeat=6):
    ss = ''.join(i)
    if ss.count('О') <= 2 and ss.count('Ц') == 1:
        k.add(ss)
print(len(k))
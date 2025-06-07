import itertools

k = 0

for i, s in enumerate(itertools.product('АБЕИЛРТФЦ', repeat=5), 1):
    if s[0] not in 'АЕИ' and s.count('Ц') == s.count('Ф') and i % 2 > 0:
        k += 1
print(k)

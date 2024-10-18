import itertools
k = 0
for i, s in enumerate(itertools.product('ЕЛОПРСТ', repeat=5), 1):
    ss = ''.join(s)
    if (ss[-1] == 'Е' or ss[-1] == 'О') and (i % 2 > 0 and ss.count('Е') + ss.count('О') >= 2):
        k+=1
print(k)
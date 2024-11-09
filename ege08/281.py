import itertools
k=0
s=''
for i in itertools.product('qwertyuiopasdfghjklzxcvbnm', repeat=5):
    k+= sum(i.count(x) for x in 'eyuioa')

print(k)
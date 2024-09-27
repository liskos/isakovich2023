import itertools


a = set()
for i in itertools.permutations('КОРАБЛИ', r=5):
    ss = ''.join(i)
    h = (ss.replace('К', '1').replace('Р', '1').replace('Б', '1').replace('Л', '1')
         .replace('О', '0').replace('А', '0').replace('И', '0'))
    if '11' not in h and '00' not in h and h[0] == '0':
        a.add(ss)
print(len(a),a)


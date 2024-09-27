import itertools


a = set()
for i in itertools.permutations('ТАРКНИЩЕ', r=6):
    ss = ''.join(i)
    h = (ss.replace('Т', '1').replace('Р', '1').replace('К', '1').replace('Н', '1')
         .replace('Е', '0').replace('А', '0').replace('И', '0').replace('Щ', '1'))
    if '11' not in h and '00' not in h and h[0] == '1':
        a.add(ss)
print(len(a),a)


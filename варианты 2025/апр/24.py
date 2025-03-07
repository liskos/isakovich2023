s = open('24.txt').read()
s = s.replace('-', '*')
while '**' in s:
    s = s.replace('**', '* *')

while '* ' in s:
    s = s.replace('* ', ' ')
while ' *' in s:
    s = s.replace(' *', ' ')

for i in range(10):
    while f'*0{i}' in s:
        s = s.replace(f'*0{i}', f'*0 {i}')
for j in range(10):
    while f' 0{j}' in s:
        s = s.replace(f' 0{j}', f' {j}')
a = sorted(s.split(), key=len, reverse=True)
for i in a[:10]:
    print(len(i), i)

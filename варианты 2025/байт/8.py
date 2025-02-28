
import itertools


for i, s in enumerate(itertools.product('абвгдеёжзийклмнопрстуфхцчшщъьэюя', repeat=6), 1):
    ss = ''.join(s)
    if ss != 'смитап':
        print(i, ss)

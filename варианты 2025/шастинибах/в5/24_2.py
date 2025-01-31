import re

s = open('24.txt').read()
a = re.findall(r"[L][^L]{0,}?[O]\w{0,}?[V][^E]{0,}?[E]", s)
print(min(map(len, a)))
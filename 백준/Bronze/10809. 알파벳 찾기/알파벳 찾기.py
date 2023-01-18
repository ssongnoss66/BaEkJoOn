s = input()

import string 
alph = list(string.ascii_lowercase)
alphLi = []

for i in alph:
    if s.count(i) > 0:
        alphLi.append(str(s.index(i)))
    else:
        alphLi.append("-1")

print(" ".join(alphLi))
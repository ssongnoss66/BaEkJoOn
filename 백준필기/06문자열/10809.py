"""10809 알파벳 찾기"""

# my ver

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

# teammate ver

for i in alph:                      # 알파벳 순회
    alphLi.append(s.find(i))        # 비워둔 리스트에 순회한 알파벳 (a, b, c ...)이 몇 개 있는지 반환 (find 매서드는 없으면 -1 반환)

print(*alphLi)

"""
import string 
alph = list(string.ascii_lowercase)

for i in alph:
    print(S.find(chr(i))) 
"""

# import string 
# string.ascii_lowercase
# .find()